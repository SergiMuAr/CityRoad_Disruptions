import tweepy
from kafka import KafkaProducer

class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        # self.counter = 0    
        super(MyStreamListener, self).__init__()
        self.kafka_producer = self.connect_kafka_producer()
        print ("KAFKA Inited")

    def publish_message(self,producer_instance, topic_name, key, value):
        try:
            key_bytes = bytes(key, encoding='utf-8')
            value_bytes = bytes(value, encoding='utf-8')
            producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
            producer_instance.flush()
            print('Message published successfully.')
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))


    def connect_kafka_producer(self):
        print ("HOLA BON DIA")
        _producer = None
        try:
            _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
        except Exception as ex:
            print('Exception while connecting Kafka')
            print(str(ex))
        finally:
            return _producer
            
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

        print ('Encountered error with status code:', status_code)
        return True # Don't kill the stream

    def on_status(self, status):
        import unidecode
        # print (status._json['retweeted_status']['extended_tweet']['full_text'])
        # text = unidecode.unidecode(status._json['retweeted_status']['extended_tweet']['full_text'])
        if 'retweeted_status' in status._json:
            if 'extended_tweet' in status._json['retweeted_status']:
                text = status._json['retweeted_status']['extended_tweet']['full_text']
            else:
                text = status._json['retweeted_status']['text']
        else:
            if 'extended_tweet' in status._json:
                text = status._json['extended_tweet']['full_text']
            else: 
                text = unidecode.unidecode(status.text)

        
        # self.counter = self.counter + 1
        self.publish_message(self.kafka_producer, 'dataStream2', 'tweet', text)
        print(text)

        
    def on_timeout(self):
        print ('Timeout...')
        return True # Don't kill the stream