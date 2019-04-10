import sys
from PreprocessText import *
from Classifier import *
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from GeoCoding import *
from kafka import KafkaConsumer
from gmaps import *
from sqlite import * 
from Twitter import initStreaming

# def initInstances():


def main():
    db = Sqlite(None)
    statistics = Sqlite('/home/sergi/CityRoad_Disruptions/statistics.db')
    db.create_table_models()
    statistics.create_table_statistics()
    gc = Geocoder()
    svm = SVMmodel()

    print ("HEYhooolaa")
    kafka = KafkaConsumer('dataStream2', auto_offset_reset='earliest',
                                bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=-1)
    # initInstances()
    for msg in kafka:        
        print ("HEYHEYEHYYYYY")
        tweet = preprocessText(msg.value.decode("utf-8"))
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