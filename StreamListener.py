import tweepy
from KafkaProd import *

class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        self.counter = 0    
        super(MyStreamListener, self).__init__()
        self.kafka_producer = KafkaClPr()

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
        
        self.counter = self.counter + 1
        print (self.counter)
        print (status._json['user']['name'], text)
        self.kafka_producer.publish_message("dataStream2", status._json['user']['name'], text)
        # self.publish_message(self.kafka_producer, 'dataStream2', 'tweet', text)

        
    def on_timeout(self):
        print ('Timeout...')
        return True # Don't kill the stream