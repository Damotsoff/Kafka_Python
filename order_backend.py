import json
import time
from kafka import KafkaProducer
from config import ORDER_KAFKA_TOPIC,ORDER_KAFKA_LIMIT,KAFKA_HOST



produser = KafkaProducer(bootstrap_servers=KAFKA_HOST)

print("Going to be generating order after 10 seconds")
print("Will generate one unique order every 10 seconds")
time.sleep(10)


for i in range(int(ORDER_KAFKA_LIMIT)):
    data = {
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i * 5,
        "items": "burger,sandwich",
    }
    produser.send(ORDER_KAFKA_TOPIC,json.dumps(data).encode('utf-8'))
    print(f"Done Sending..{i}")
