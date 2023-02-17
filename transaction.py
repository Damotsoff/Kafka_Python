import json
from kafka import KafkaProducer
from kafka import KafkaConsumer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(ORDER_KAFKA_TOPIC, bootstrap_server="localhost:29092")
producer = KafkaProducer(bootstrap_server="localhost:29092")


print("Gonna start listening")

while True:
    for message in consumer:
        print("Ongoing transaction..")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
        user_id = consumed_message["user_id"]
        total_costs = consumed_message["total_costs"]
        data = {
            "user_id": user_id,
            "total_costs": total_costs,
            "customer_email": f"{user_id}@gmail.com",
        }
        print("Successful transaction..")
        producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
