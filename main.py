import sys
from PreprocessText import *
from Classifier import *
from GeoCoding import *
from kafka import KafkaConsumer
from gmaps import *
from sqlite import * 

class Executable:
    def __init__(self):
        self.listOfChannels = ["988457597241118720","123851794", "412411621", "262606630", "59775384", "18577646", "7679392", "155930023", "110647916", "28373820", "8330472", "27477225", "274008117", "110946158", "110946582", "121146038", "112385035", "115624105", "423369901", "23791197"]

        self.db = Sqlite(None)
        self.db.create_table_models()
        self.statistics = Sqlite('/home/sergi/CityRoad_Disruptions/statistics.db')
        self.statistics.create_table_statistics()
        self.gc = Geocoder()
        self.svm = SVMmodel()
        self.nlp = NLP()
        self.gm = Gmaps()
        self.kafka = KafkaConsumer('dataStream2', auto_offset_reset='earliest',
                                    bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=-1)

    def execute(self):
        for msg in self.kafka: 
            tweet = msg.value.decode("utf-8")  
            author = msg.key.decode("utf-8")
            print (author)
            isTI = self.svm.predictText(self.nlp.prepareToClf(tweet))
            ubicat = False
            isGob = False
            isInd = False
            if isTI:
                twLines = tweet.split("\n")
                for line in twLines:
                    geoloc = self.gc.geoCode(line)
                    if geoloc is not None:
                        model = (self.nlp.prepareToVisualize(tweet), geoloc["lat"], geoloc["lng"])
                        self.db.insert_model(model) 
                        incidencies = self.db.selectGeoloc()
                        self.gm.visualizeMap (incidencies)
                        ubicat = True
                if not ubicat:
                    model = (self.nlp.prepareToVisualize(tweet), None, None)
                    self.db.insert_model (model)
            
            if author in self.listOfChannels:
                isGob = True
            else:
                isInd = True
            stat = (tweet,isTI,isGob,isInd,ubicat) 
            print ("FAIG INSERT STAT", stat)
            self.statistics.insert_stat(stat)

if __name__ == '__main__':
    ex = Executable()
    ex.execute()
