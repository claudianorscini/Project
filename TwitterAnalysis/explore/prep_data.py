import tweepy
import json
import time
from datetime import datetime
import pandas as pd
import re

# Initializing a listener class that streams Twitter status
class StdOutListener(tweepy.StreamListener):
#     Create an init statement
    def __init__(self, start_time, time_limit=100):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []

#    Defining what you are going to do based on data
    def on_data(self, data):
        try:
#             Opening data for streaming
            with open('output.json', 'a') as f:
                f.write(data)
                return True
        except KeyboardInterrupt:
            print("Twitter Download is interrupted")
        except BaseException as e:
            print(str(e))
        return True

    def on_error(self, status):
        print status


def create_tweets_data(tweets_data_path):
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")

    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    # Printing the length of the tweets data
    print len(tweets_data)
    return tweet,tweets_data

def gettext(tweet,element):
    try:
        return tweet[element]
    except KeyError:
        pass


def classify_text(tweet,tweets_data):
    # Getting the data and texts along the ways using gettext
    tweets = pd.DataFrame()
    tweets['text'] = [gettext(tweet,'text') for tweet in tweets_data]
    tweets['lang'] = [gettext(tweet,'lang') for tweet in tweets_data]
    tweets['created_at'] = [gettext(tweet,'created_at') for tweet in tweets_data]
    tweets['created_at'] = pd.to_datetime(tweets['created_at'],errors='ignore')
    tweets.set_index('created_at',inplace=True)
    tweets.dropna(axis=0,how="any",inplace=True)
    tweets.isnull().sum()
    return tweets



def word_in_text(word, text):
    try:
        text = text.lower()
        match = re.search(word, text)
        if match:
            return True
        return False
    except AttributeError:
        return False
