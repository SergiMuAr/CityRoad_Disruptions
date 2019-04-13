import sys
from PreprocessText import *
from Classifier import *
from GeoCoding import *
from kafka import KafkaConsumer
from gmaps import *
from sqlite import * 


db = Sqlite(None)
db.create_table_models()
statistics = Sqlite('/home/sergi/CityRoad_Disruptions/statistics.db')
statistics.create_table_statistics()
gc = Geocoder()
svm = SVMmodel()
nlp = NLP()
gm = Gmaps()
kafka = KafkaConsumer('dataStream2', auto_offset_reset='earliest',
                            bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=-1)

def main():
    for msg in kafka: 
        tweet = msg.value.decode("utf-8")  
        isTI = svm.predictText(nlp.prepareToClf(tweet))
        ubicat = False
        if isTI:
            twLines = tweet.split("\n")
            for line in twLines:
                geoloc = gc.geoCode(line)
                if geoloc is not None:
                    model = (nlp.prepareToVisualize(tweet), geoloc["lat"], geoloc["lng"])
                    db.insert_model(model) 
                    incidencies = db.selectGeoloc()
                    gm.visualizeMap (incidencies)
                    ubicat = True
            if not ubicat:
                model = (nlp.prepareToVisualize(tweet), None, None)
                db.insert_model (model)
        
        # if name in list:
            # isGob = True
        # else:
            # isInd = True
        # stat = (tweet,isTI,isGob,isInd,ubicat) 
        # print ("FAIG INSERT STAT", stat)
        # statistics.insert_stat(stat)
if __name__ == '__main__':
    main()