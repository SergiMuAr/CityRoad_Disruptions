from kafka import KafkaConsumer

class KafkaClCns:
    def __init__(self):
        self.consumer = KafkaConsumer('dataStream2', auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=-1)

    def subscribe(self):
        return self.consumer