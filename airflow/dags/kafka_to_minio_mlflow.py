from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Inside Docker network:
# - Kafka broker: kafka:9092
# - MinIO: http://minio:9000 (admin / adminadmin)
# - MLflow: http://mlflow:5000

def consume_to_minio_and_log():
    import io, csv, time
    from kafka import KafkaConsumer
    import boto3
    import mlflow

    # 1) Consume up to 20 messages or stop after 5s idle
    consumer = KafkaConsumer(
        "reviews_raw",
        bootstrap_servers=["kafka:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        consumer_timeout_ms=5000,
    )
    rows = []
    for msg in consumer:
        rows.append([msg.timestamp, msg.value.decode("utf-8")])
        if len(rows) >= 20:
            break
    consumer.close()

    # 2) Build a small CSV in memory
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["ts", "text"])
    w.writerows(rows)
    body = buf.getvalue().encode("utf-8")

    # 3) Upload to MinIO -> bucket 'bronze', key 'kafka/demo_<ts>.csv'
    s3 = boto3.client(
        "s3",
        endpoint_url="http://minio:9000",
        aws_access_key_id="admin",
        aws_secret_access_key="adminadmin",
        region_name="us-east-1",
    )
    s3.put_object(Bucket="bronze", Key=f"kafka/demo_{int(time.time())}.csv", Body=body)

    # 4) Log to MLflow
    mlflow.set_tracking_uri("http://mlflow:5000")
    with mlflow.start_run(run_name="kafka_ingest_demo"):
        mlflow.log_metric("messages_ingested", len(rows))

with DAG(
    dag_id="kafka_to_minio_mlflow",
    start_date=datetime(2024, 1, 1),
    schedule=None,     # trigger manually
    catchup=False,
    tags=["demo", "kafka", "minio", "mlflow"],
) as dag:
    PythonOperator(
        task_id="consume_push_log",
        python_callable=consume_to_minio_and_log,
    )
