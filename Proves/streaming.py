import tweepy
import csv
import configparser
config = configparser.ConfigParser()
config.read('/home/sergi/Documents/config.ini')
auth = tweepy.OAuthHandler(config['api.keys']['TWITTER_CONSUMER_KEY'], config['api.keys']['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(config['api.keys']['TWITTER_AUTH_TOKEN_KEY'], config['api.keys']['TWITTER_AUTH_SECRET'])
api = tweepy.API(auth)

print (api)
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

    def on_status(self, status):
        print(status.text)


#---------------------------------------------------#

# for status in tweepy.Cursor(api.user_timeline, screen_name='@transit').items():
#     print (status._json['text'])

# # Open/create a file to append data to
# csvFile = open('guardiaUrbana.csv', 'a')

# #Use csv writer
# csvWriter = csv.writer(csvFile)

# # # Els RT's no els retorna sencers moltes vegades
# # for status in tweepy.Cursor(api.user_timeline, screen_name='@transit', tweet_mode = 'extended').items(500):
# #     # Write a row to the CSV file. I use encode UTF-8
# #     # csvWriter.writerow([tweet.created_at, tweet.text])
# #     print (status.full_text)
# # csvFile.close()
# for tweet_info in tweepy.Cursor(api.user_timeline, screen_name='@barcelona_GUB', tweet_mode='extended').items(500):
#     if 'retweeted_status' in dir(tweet_info):
#         tweet=tweet_info.retweeted_status.full_text
#     else:
#         tweet=tweet_info.full_text
#     # print (tweet)
#     csvWriter.writerow([tweet])
# csvFile.close()
