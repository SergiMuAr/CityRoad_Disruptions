import sys
from Preprocess import *
from TopicModel import *
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from GeoCoding import *
from kafka import KafkaConsumer, KafkaProducer
import json
from gmaps import *
from sqlite import * 

# def main(args=sys.argv[1:]):
#     df = args[0]
#     preprocess (df)
def main():
    db = Sqlite()
    db.create_table_models()
    gc = Geocoder()
    svm = SVMmodel()
    consumer = KafkaConsumer('dataStream2', auto_offset_reset='earliest',
                                bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=-1)
    for msg in consumer:
        tweet = msg.value
        isIT = svm.predictText(tweet)
        print (isIT)
        if (isIT):
            tweet = tweet.decode("utf-8")
            tweets = tweet.split("\n")
            for tw in tweets:
                geoloc = gc.geoCode(tw)
                print (geoloc)
                # add to database
                model = (tw, geoloc["lat"], geoloc["lng"])
                model_id = db.insert_row (model) 
                print (model_id)
                # visualitzar incidencia
                incidencies = db.selectAll()
                visualizeMap (incidencies)
                
                
    
if __name__ == '__main__':
    main()