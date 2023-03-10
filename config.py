from configparser import ConfigParser

CONFIG = ConfigParser()
CONFIG.read("config.ini")
ORDER_KAFKA_TOPIC = CONFIG["KAFKA"]["ORDER_KAFKA_TOPIC"]
ORDER_CONFIRMED_KAFKA_TOPIC = CONFIG["KAFKA"]["ORDER_CONFIRMED_KAFKA_TOPIC"]
ORDER_KAFKA_LIMIT = CONFIG["KAFKA"]["ORDER_KAFKA_LIMIT"]
KAFKA_HOST = CONFIG["KAFKA"]["KAFKA_HOST"]
REDIS_HOST = CONFIG["REDIS"]["REDIS_HOST"]
REDIS_PORT = CONFIG["REDIS"]["REDIS_PORT"]