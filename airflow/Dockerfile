FROM apache/airflow:2.9.3

# Install as the "airflow" user (not root) and pin to Airflow's constraints
USER airflow

ARG AIRFLOW_VERSION=2.9.3
ARG PYTHON_VERSION=3.11
ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

RUN pip install --no-cache-dir --constraint "${CONSTRAINT_URL}" \
    kafka-python mlflow boto3
