from kafka import KafkaProducer

class KafkaClPr:

    def __init__(self):
        self.producer = self.connect_kafka_producer()
        pass
    
    def publish_message(self, topic_name, key, value):
        try:
            key_bytes = bytes(key, encoding='utf-8')
            value_bytes = bytes(value, encoding='utf-8')
            self.producer.send(topic_name, key=key_bytes, value=value_bytes)
            self.producer.flush()
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))


    def connect_kafka_producer(self):
        _producer = None
        try:
            _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
        except Exception as ex:
            print('Exception while connecting Kafka')
            print(str(ex))
        finally:
            return _producer
