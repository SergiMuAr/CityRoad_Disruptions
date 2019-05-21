import tweepy
import csv
import configparser
from StreamListener import * 

class Twitter:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('/home/sergi/Documents/config.ini')
        auth = tweepy.OAuthHandler(config['api.keys']['TWITTER_CONSUMER_KEY'], config['api.keys']['TWITTER_CONSUMER_SECRET'])
        auth.set_access_token(config['api.keys']['TWITTER_AUTH_TOKEN_KEY'], config['api.keys']['TWITTER_AUTH_SECRET'])
        self.api = tweepy.API(auth, wait_on_rate_limit=True)
        self.myStreamListener = MyStreamListener()
        
    def stalk(self):
        listOfChannels = ["988457597241118720","123851794", "412411621", "262606630", "59775384", "18577646", "7679392", "155930023", "110647916", 
        "28373820", "8330472", "27477225", "274008117", "110946158", "110946582", "121146038", "112385035", "115624105", "423369901", "23791197"]
        myStream = tweepy.Stream(auth = self.api.auth, listener=self.myStreamListener, tweet_mode = 'extended')
        # myStream.filter(languages = ['ca'], track=['accident','cua', 'cues', 'incidencia','incident', 'retenció', 'retencions','transit','trafic', 'aturada', 'aturat', 'aturats', 'circulacio', 'circulació', 'carril','via', 'alteració', 'desviament', 'tallat', 'tallada', 'tall', 'tancat'], 
        #             follow = listOfChannels)      
        myStream.filter(follow = ["988457597241118720"])      
    
if __name__ == '__main__':
    tw = Twitter()
    tw.stalk()