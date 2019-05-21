import tweepy
import csv
import configparser
from kafka import KafkaConsumer, KafkaProducer

config = configparser.ConfigParser()
config.read('/home/sergi/Documents/config.ini')
auth = tweepy.OAuthHandler(config['api.keys']['TWITTER_CONSUMER_KEY'], config['api.keys']['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(config['api.keys']['TWITTER_AUTH_TOKEN_KEY'], config['api.keys']['TWITTER_AUTH_SECRET'])
api = tweepy.API(auth, wait_on_rate_limit=True)

print (api)
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

    def fesAlgo(self):
        print ('faig algo')
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

        print ('Encountered error with status code:', status_code)
        return True # Don't kill the stream

    def on_status(self, status):
        text = status.text
        location = "ini"
        geo = "ini"
        if hasattr(status, "location"):
            location = status.location

        if hasattr(status,"geo_enable"):
            geo = status.geo_enable
        
        kafka_producer = self.connect_kafka_producer()
        self.publish_message(kafka_producer, 'topic_test', 'tw', status.text)
        if kafka_producer is not None:
            kafka_producer.close()
        self.fesAlgo()
        print(status.text, location, geo)
        
    def on_timeout(self):
        print ('Timeout...')
        return True # Don't kill the stream

# Create a streaming API and set a timeout value of 60 seconds.

# streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

# # Optionally filter the statuses you want to track by providing a list
# # of users to "follow".

# print >> sys.stderr, 'Filtering the public timeline for "%s"' % (' '.join(sys.argv[1:]),)

# streaming_api.filter(follow=None, track=Q)


#---------------------------------------------------#

# for status in tweepy.Cursor(api.user_timeline, screen_name='@transit').items():
#     print (status._json['text'])

# # Open/create a file to append data to
# csvFile = open('guardiaUrbana.csv', 'a')

# #Use csv writer
# csvWriter = csv.writer(csvFile)

# # # Els RT's no els retorna sencers moltes vegades
# # for status in tweepy.Cursor(api.user_timeline, screen_name='@transit', tweet_mode = 'extended').items(500):
# #     # Write a row to the CSV file. I use encode UTF-8
# #     # csvWriter.writerow([tweet.created_at, tweet.text])
# #     print (status.full_text)
# # csvFile.close()
# for tweet_info in tweepy.Cursor(api.user_timeline, screen_name='@barcelona_GUB', tweet_mode='extended').items(500):
#     if 'retweeted_status' in dir(tweet_info):
#         tweet=tweet_info.retweeted_status.full_text
#     else:
#         tweet=tweet_info.full_text
#     # print (tweet)
#     csvWriter.writerow([tweet])
# csvFile.close()
