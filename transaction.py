import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from config import ORDER_CONFIRMED_KAFKA_TOPIC, ORDER_KAFKA_TOPIC, HOST

consumer = KafkaConsumer(ORDER_KAFKA_TOPIC, bootstrap_servers=HOST)
producer = KafkaProducer(bootstrap_servers=HOST)


print("Gonna start listening")

while True:
    for message in consumer:
        print("Ongoing transaction..")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
        user_id = consumed_message["user_id"]
        total_cost = consumed_message["total_cost"]
        data = {
            "user_id": user_id,
            "total_cost": total_cost,
            "customer_email": f"{user_id}@gmail.com",
        }
        print("Successful transaction..")
        producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
