import tweepy
import csv
import configparser
from StreamListener import * 

def initStreaming():
    config = configparser.ConfigParser()
    config.read('/home/sergi/Documents/config.ini')
    auth = tweepy.OAuthHandler(config['api.keys']['TWITTER_CONSUMER_KEY'], config['api.keys']['TWITTER_CONSUMER_SECRET'])
    auth.set_access_token(config['api.keys']['TWITTER_AUTH_TOKEN_KEY'], config['api.keys']['TWITTER_AUTH_SECRET'])
    api = tweepy.API(auth)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode = 'extended')
    # myStream.filter(follow = ["274008117"])
    # jo, tmbinfo, 
    # myStream.filter(track=['accident, cua, cues, incidencia, incident, retenció, retencions, transit, trafic, aturada, aturat, aturats, circulacio, circulació, carril, via, alteració, desviament, tallat, tallada, tall, tancat'], 
    #                 follow = ["988457597241118720","1116634987", "274008117"])
    myStream.filter(languages = ['ca'], track=['cua', 'cues', 'incidencia', 'retenció', 'retencions', 'aturada', 'aturat', 'aturats', 'circulacio', 'circulació', 'carril', 'alteració', 'desviament', 'tallat', 'tallada', 'tall', 'tancat'], 
                follow = ["988457597241118720"])
    # myStream.filter(track=['cua, cues, incidencia, incident, ⚠, 🚗, retenció, retencions, transit, trafic, aturada, aturat, circulacio, lenta, lent, carril, via, alteració, desviament, tallat, tallada, tancat'], 
    #                 follow = ["988457597241118720"])

    
if __name__ == '__main__':
    initStreaming()