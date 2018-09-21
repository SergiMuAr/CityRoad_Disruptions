import tweepy
import csv
auth = tweepy.OAuthHandler("Hdah781zeulKrfrMzK3iI6GTs", "tFLvGas5hrXwq4yiXheQj5On99VUoAl5Fpcl6vRQqatjxISFDZ")
auth.set_access_token("988457597241118720-NIGfC9gqlNakSIcmDZfVAvb5LZHDgqa", "SyoofoDP3GJsDhRFHdjjsIMAFLp2XwBYXakVyUhb3YvAE")

api = tweepy.API(auth)

print (api)

# for status in tweepy.Cursor(api.user_timeline, screen_name='@transit').items():
#     print (status._json['text'])

# Open/create a file to append data to
csvFile = open('resultsTransit2.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)


for status in tweepy.Cursor(api.user_timeline, screen_name='@transit', tweet_mode = 'extended').items(500):
    # Write a row to the CSV file. I use encode UTF-8
    # csvWriter.writerow([tweet.created_at, tweet.text])
    print (status.full_text)
csvFile.close()
