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
```

parameters.yml
```yaml
KAFKA_SERVERS: ark-01.srvs.cloudkafka.com:9094,ark-02.srvs.cloudkafka.com:9094,ark-03.srvs.cloudkafka.com:9094
KAFKA_USERNAME: my_user
KAFKA_PASSWORD: my_pass
```

example.py
```python
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

```