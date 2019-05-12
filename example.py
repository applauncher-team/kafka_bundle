from applauncher.kernel import Environments, Kernel
from kafka_bundle import KafkaBundle, KafkaManager
import inject
from time import sleep


bundle_list = [
    KafkaBundle()
]


def consumer_callback(message):
    print("MESSAGE", message.value())

with Kernel(Environments.DEVELOPMENT, bundle_list) as kernel:
    km = inject.instance(KafkaManager)
    km.subscribe(
        topics=["my_user-text"],
        group_id="test",
        consumer_callback=consumer_callback
    )
    sleep(1)
    km.produce("my_user-text", "TEST")
    print("Message sent")
    input("press enter to exit")
