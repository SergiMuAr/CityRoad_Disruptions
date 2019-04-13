import tweepy
import csv
import configparser
from StreamListener import * 

listOfChannels = ["988457597241118720","123851794", "412411621", "262606630", "59775384", "18577646", "7679392", "155930023", "110647916", "28373820", "8330472", "27477225", "274008117", "110946158", "110946582", "121146038", "112385035", "115624105", "423369901", "23791197"]

def initStreaming():
    config = configparser.ConfigParser()
    config.read('/home/sergi/Documents/config.ini')
    auth = tweepy.OAuthHandler(config['api.keys']['TWITTER_CONSUMER_KEY'], config['api.keys']['TWITTER_CONSUMER_SECRET'])
    auth.set_access_token(config['api.keys']['TWITTER_AUTH_TOKEN_KEY'], config['api.keys']['TWITTER_AUTH_SECRET'])
    api = tweepy.API(auth)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode = 'extended')
    # jo, tmbinfo, equipviari
    myStream.filter(languages = ['ca'], track=['accident, cua, cues, incidencia, incident, retenció, retencions, transit, trafic, aturada, aturat, aturats, circulacio, circulació, carril, via, alteració, desviament, tallat, tallada, tall, tancat'], 
                    follow = listOfChannels)
    # myStream.filter(languages = ['ca'], track=['cua', 'cues', 'incidencia', 'retenció', 'retencions', 'aturada', 'aturat', 'aturats', 'circulacio', 'circulació', 'carril', 'alteració', 'desviament', 'tallat', 'tallada', 'tall', 'tancat'], 
    #             follow = ["988457597241118720"])
    # myStream.filter(track=['cua, cues, incidencia, incident, ⚠, 🚗, retenció, retencions, transit, trafic, aturada, aturat, circulacio, lenta, lent, carril, via, alteració, desviament, tallat, tallada, tancat'], 
    #                 follow = ["988457597241118720"])

    
if __name__ == '__main__':
    initStreaming()