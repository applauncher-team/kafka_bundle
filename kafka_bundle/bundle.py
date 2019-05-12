import logging
from applauncher.kernel import Configuration, Kernel, ConfigurationReadyEvent
import inject
from confluent_kafka import Producer, Consumer

class KafkaException(Exception):
    pass

def delivery_callback(err, msg):
    if err:
        raise KafkaException(err)
    print(msg)

class KafkaManager(object):
    def __init__(self, config):
        self.config = config
        self.default_producer = self.get_producer()

    def produce(self, topic, message, wait=False):
        self.default_producer.produce(topic, message, callback=delivery_callback)

    def get_producer(self):
        return Producer(**self.config)

    def get_consumer(self, group_id):
        c = dict(self.config)
        c["group.id"] = group_id
        return Consumer(**c)


def applauncher_config_to_confluent(config):
    c = {}
    for k, v in config._asdict().items():
        k = k.replace("_", ".")
        if v.__class__.__name__ == "Configuration":
            c[k] = applauncher_config_to_confluent(v)
        else:
            c[k] = v
    return c

class KafkaBundle(object):
    def __init__(self):
        self.logger = logging.getLogger("kafka")
        self.config_mapping = {
            "kafka": {
                'bootstrap_servers': None,
                'session_timeout_ms': 6000,
                'default_topic_config': {'auto_offset_reset': 'smallest'},
                'security_protocol': 'SASL_SSL',
                'sasl_mechanisms': 'SCRAM-SHA-256',
                'sasl_username': None,
                'sasl_password': None

            }
        }

        self.event_listeners = [
            (ConfigurationReadyEvent, self.config_ready),
        ]

        self.injection_bindings = {}

    def config_ready(self, event):
        kafka_config = applauncher_config_to_confluent(event.configuration.kafka)
        self.injection_bindings[KafkaManager] = KafkaManager(kafka_config)
