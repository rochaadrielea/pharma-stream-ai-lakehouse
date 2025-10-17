from kafka import KafkaProducer, KafkaConsumer

bootstrap = ["localhost:9092"]

p = KafkaProducer(bootstrap_servers=bootstrap)
p.send("reviews_raw", b"hello from python"); p.flush()

c = KafkaConsumer("reviews_raw", bootstrap_servers=bootstrap,
                  auto_offset_reset="earliest", enable_auto_commit=False)
print(next(c).value)  # should print one of your messages
c.close()
p.close()