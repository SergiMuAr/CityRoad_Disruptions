import sys
from PreprocessText import *
from Classifier import *
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
    db = Sqlite(None)
    statistics = Sqlite('/home/sergi/CityRoad_Disruptions/statistics.db')
    db.create_table_models()
    gc = Geocoder()
    svm = SVMmodel()
    consumer = KafkaConsumer('dataStream2', auto_offset_reset='earliest',
                                bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=-1)
    for msg in consumer:        
        tweet = preprocessText(msg.value.decode("utf-8"))
        # tweet = msg.value.decode("utf-8")
        print (tweet)
        isIT = svm.predictText(tweet)
        print (isIT)
        if (isIT):
            tweetaux = msg.value.decode("utf-8")
            tweets = tweetaux.split("\n")
            for tw in tweets:
                geoloc = gc.geoCode(tw)
                print (tw)
                print (geoloc)
                # add to database
                if (geoloc is not None):
                    model = (msg.value, geoloc["lat"], geoloc["lng"])
                    model_id = db.insert_row (model) 
                    # visualitzar incidencia
                    # print ("VISUALITZO", tw)
                    incidencies = db.selectAll()
                    visualizeMap (incidencies)
                
                
    
if __name__ == '__main__':
    main()