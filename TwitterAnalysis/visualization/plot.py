import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
# Adjusting the size of matplotlib
import matplotlib.pylab as mpl


def plot_by_lang(tweets):
    mpl.rc('figure', figsize=(8, 7))
    mpl.__version__
    # Adjusting the style of matplotlib
    style.use('ggplot')

    tweets_by_lang = tweets['lang'].value_counts()
    tweets_by_lang.head(10).plot(kind="bar")
    #mpl.show()


def plot_by_name(tweets_by_word, filt_names):

    mpl.rc('figure', figsize=(8, 7))
    mpl.__version__
    # Adjusting the style of matplotlib
    style.use('ggplot')
    # Plotting the word counts
    candidate_frame = pd.DataFrame([tweets_by_word], columns = filt_names)
    candidate_frame.T.plot(kind='bar',legend=False,title="Twitter counts per word")
    mpl.show()
def plot_by_date(word_by_date):
    mpl.rc('figure', figsize=(8, 7))
    mpl.__version__
    # Adjusting the style of matplotlib
    style.use('ggplot')

    pd.concat(word_by_date, axis=1).plot(kind='bar')
    mpl.show()
