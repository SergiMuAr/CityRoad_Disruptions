import sys
from Preprocess import *
from TopicModel import *
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from GeoCoding import *
from Twitter import *
from kafka import KafkaConsumer, KafkaProducer
import json


# def main(args=sys.argv[1:]):
#     df = args[0]
#     preprocess (df)
def main():
    # gc = Geocoder()
    # svm = SVMmodel()
    # print ("HOLA1")
    # myStreamListener = MyStreamListener()
    # myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    # myStream.filter(follow = ["988457597241118720"])
    print ("HOLA")
    consumer = KafkaConsumer('dataStream', auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=-1)
    for msg in consumer:
        print (msg.value)
        # record = json.loads(msg.value)
        # print (record)
        # record = json.loads(msg.value)
        # calories = int(record['calories'])
        # title = record['title']
        # isIT = svm.predictText(tweet)
        # gc.geoCode(tweet)

    
if __name__ == '__main__':
    main()