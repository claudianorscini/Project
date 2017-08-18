from textblob import TextBlob
import pandas as pd

def find_polarity(tweet):
    try:
        return TextBlob(tweet).polarity
    except:
        pass

def find_subjectivity(tweet):
    try:
        return TextBlob(tweet).subjectivity
    except:
        pass

def apply_textblob(tweets):
        # Applying textblob to each tweets text
    tweets['polarity'] = tweets['text'].apply(lambda tweet:find_polarity(tweet))
    tweets['subjectivity'] = tweets['text'].apply(lambda tweet:find_subjectivity(tweet))
    tweets.head()
    tweets['polaritytext'] =  pd.cut(tweets.polarity, 3,labels=["unhappy","neutral","happy"])
    tweets['subjectivitytext'] =  pd.cut(tweets.subjectivity, 2,labels=["meaningful","subjective"])
    return tweets
