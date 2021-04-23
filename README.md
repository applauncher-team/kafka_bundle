# kafka_bundle
Just a binding to use kafka in applauncher. Minimal configuration example:
# Installing
```bash
pip install kafka_bundle
```

# Using

configuration.yml
```yaml
kafka:
  bootstrap_servers: {KAFKA_SERVERS}
  sasl_username: {KAFKA_USERNAME}
  sasl_password: {KAFKA_PASSWORD}
  group_id: {KAFKA_GROUP_ID}
```

parameters.yml
```yaml
KAFKA_SERVERS: ark-01.srvs.cloudkafka.com:9094,ark-02.srvs.cloudkafka.com:9094,ark-03.srvs.cloudkafka.com:9094
KAFKA_USERNAME: my_user
KAFKA_PASSWORD: my_pass
KAFKA_GROUP_ID: test
```

example.py
```python
from applauncher import Kernel, event
from kafka_bundle import KafkaBundle, consumer_reader, KafkaContainer


class ExampleBundle:
    def __init__(self):

        self.services = [
            ("messag_reader", self.run, [], {})
        ]

    def run(self):
        consumer = KafkaContainer.consumer()
        print(consumer)
        topic = "x27ltgva-my_event"
        producer = KafkaContainer.producer()
        # Sending a message
        producer.produce(topic, b"Hi")
        print(producer)
        producer.flush()
        # Message reader
        consumer.subscribe(topics=[topic])
        for msg in consumer_reader(consumer):
            print(msg.value())



with Kernel(bundles=[ExampleBundle(), KafkaBundle()], environment="PROD") as kernel:
    kernel.wait()
```