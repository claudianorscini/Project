import sys
import tweepy
import pandas as pd
import json
import time
import explore.prep_data as pr
import visualization.plot as vis
import explore.login as login
import explore.sentiment as sent
import shutil
import matplotlib.pyplot as plt
filt_names = ['renzi', 'salvini', 'grillo']

name= ''
for filt_name in filt_names:
    name = name + '_' + filt_name


def createDB():

    # authentication
    auth = login.authentication()

    # reading all data from start time
    start_time = time.strptime("10 Aug 17", "%d %b %y")
    l = pr.StdOutListener(start_time)
    stream = tweepy.Stream(auth, l)
    #capture data by the keywords: 'trump', 'hillary'
    try:
        stream.filter(track= filt_names)
    except KeyboardInterrupt:
        print("Twitter Download is interrupted")

    shutil.copy2('output.json','output_'+ name +'.json')


def readDB():
    tweets_data_path = ('output_' + name + '.json')
    tweet, tweets_data = pr.create_tweets_data(tweets_data_path)
    tweets = pr.classify_text(tweet,tweets_data)
    vis.plot_by_lang(tweets)

    tweets_by_word=[]
    word_by_date=[]
    for filt_name in filt_names:
        tweets[filt_name] = tweets['text'].apply(lambda tweet: pr.word_in_text(filt_name, tweet))
        #print tweets[filt_name]
        tweets_by_word.append(tweets[filt_name].value_counts()[1])
        #groupbydate = ('tweets.'+ filt_name + '.groupby(tweets.index.date).sum()')
        #word_by_date.append(eval(groupbydate))
    #print word_by_date
    print((tweets_by_word))

    #vis.plot_by_name(tweets_by_word,filt_names)
    #vis.plot_by_date(word_by_date)
    tweets.to_pickle('prep_data'+ name +'.pkl')
  # load it
def sentiment_analysis():
    tweets = pd.read_pickle('prep_data' + name + '.pkl')
    tweets = sent.apply_textblob(tweets)
    polaritycnt= []

    for filt_name in filt_names:
        tweets_per_word = tweets[eval('tweets.'+ filt_name +'==True')]
        polarity_name= 'polarity_'+ filt_name
        polarity_name = tweets_per_word['polaritytext'].value_counts().rename(filt_name)
        polaritycnt.append(polarity_name)

    polarity_tot=pd.concat(polaritycnt,axis=1)

    print polarity_tot
    for filt_name in filt_names:

        polarity_tot[ filt_name +'ratio'] = eval('polarity_tot.' + filt_name) \
        /eval('polarity_tot.'+ filt_name +'.sum()')
        print polarity_tot[filt_name + 'ratio']
    polarity_tot.loc[:,'renziratio':'grilloratio'].T.plot(kind='bar',stacked=True,rot=1)
    plt.show()
def all():
    createDB()
    readDB()
    sentiment_analysis()


if __name__ =="__main__":
    argv = sys.argv

    if argv[1] == "all":
        all()

    elif argv[1] == "createDB":
        createDB()

    elif argv[1] == "readDB":
        readDB()

    elif argv[1] == "sentiment_analysis":
        sentiment_analysis()

    else:
        print 'Error'
