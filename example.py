from applauncher import Kernel, event
from kafka_bundle import KafkaBundle, consumer_reader, KafkaContainer


class ExampleBundle:
    def __init__(self):

        self.services = [
            ("get_emails", self.run, [], {})
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
