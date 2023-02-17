import json
import time
from kafka import KafkaProducer


ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 2000
produser = KafkaProducer(bootstrap_servers="localhost:29092")

print("Going to be generating order after 10 seconds")
print("Will generate one unique order every 10 seconds")
time.sleep(10)


for i in range(ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i * 5,
        "items": "burger,sandwich",
    }
    produser.send(ORDER_KAFKA_TOPIC,json.dumps(data).encode('utf-8'))
    print(f"Done Sending..{i}")
    time.sleep(3)
