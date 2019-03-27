import tweepy
import csv
import configparser
from kafka import KafkaConsumer, KafkaProducer

config = configparser.ConfigParser()
config.read('/home/sergi/Documents/config.ini')
auth = tweepy.OAuthHandler(config['api.keys']['TWITTER_CONSUMER_KEY'], config['api.keys']['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(config['api.keys']['TWITTER_AUTH_TOKEN_KEY'], config['api.keys']['TWITTER_AUTH_SECRET'])
api = tweepy.API(auth)

print (api)

def initListener():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode = 'extended')
    myStream.filter(follow = ["988457597241118720"])

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

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

        location = "ini"
        geo = "ini"
        if hasattr(status, "location"):
            location = status.location

        if hasattr(status,"geo_enable"):
            geo = status.geo_enable
        
        kafka_producer = self.connect_kafka_producer()
        self.publish_message(kafka_producer, 'dataStream2', 'tweet', text)
        if kafka_producer is not None:
            kafka_producer.close()
        print(text, location, geo)
        
    def on_timeout(self):
        print ('Timeout...')
        return True # Don't kill the stream


initListener()