import json
import redis
from kafka import KafkaConsumer
from config import ORDER_CONFIRMED_KAFKA_TOPIC, KAFKA_HOST, REDIS_HOST, REDIS_PORT

pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=0)
gmail_database = redis.Redis(connection_pool=pool)
ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"
consumer = KafkaConsumer(ORDER_CONFIRMED_KAFKA_TOPIC, bootstrap_servers=KAFKA_HOST)

emails_sent_so_far = set()
print("Gonna start listening")

while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        customer_email = consumed_message["customer_email"]
        user_id = consumed_message["user_id"]
        print(f"Sending email to {customer_email} ")
        emails_sent_so_far.add(customer_email)
        print(f"So far emails sent to {len(emails_sent_so_far)} unique emails")
        gmail_database.set(user_id,customer_email)
        print("Add to db!")
