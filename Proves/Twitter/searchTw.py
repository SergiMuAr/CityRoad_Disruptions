import tweepy
import csv
import configparser

# Handle api Auth protocol with configparser
config = configparser.ConfigParser()
config.read('/home/sergi/Documents/config.ini')
auth = tweepy.OAuthHandler(config['api.keys']['TWITTER_CONSUMER_KEY'], config['api.keys']['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(config['api.keys']['TWITTER_AUTH_TOKEN_KEY'], config['api.keys']['TWITTER_AUTH_SECRET'])
api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('searchOut.csv', 'w')

#Use csv writer
csvWriter = csv.writer(csvFile)

# filter out retweets and look for keywords
# query = "-filter:retweets accident OR cua OR cues OR incidencia OR incident OR retencio OR rentencions OR transit OR trafic OR aturada OR aturat OR aturats OR circulacio OR circulació OR carril OR via OR alteració OR desviament OR tallat OR tallada OR tall OR tancat)" 
query = "transit OR trafic"
for tweet in tweepy.Cursor(api.search, q=query, geocode = "41.5,2.0,100km", exclude_replies = True, tweet_mode = "extended").items(999):
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text) and (tweet.metadata['iso_language_code'] == "ca"):
        csvWriter.writerow([tweet.full_text]) 

csvFile.close()
print ("Work Done!")