import sys
import db.db_proc as db
import processor.download as dn
import processor.wordcount as wordcount
import visualization.plot.plots as plot
import operator as op
#import plot.plot as plot
import numpy as np


def download():
    # fetch url from the db
    docs = db.get_data('document')
    for doc in docs:

        # step 1. download the raw text
        title, body = dn.get_data(doc['URL'])
        db.save_raw_text( doc['Id'], title, body )



def tf():
    # fetch url from the db
    docs = db.get_data('document')
    db.delete_data_from_table( 'wordcount' )

    for doc in docs:

        # step 2. count the Words_count
        tf,tf_norm = wordcount.tf(doc['raw_text'])
        db.insert_term_freq( doc['Id'], tf, tf_norm )

def tot_tfdf():
    # fetch url from the db
    docs = db.get_data('document')
    result_1={}
    result_2={}
    result_3={}
    n_doc=0
    for doc in docs:
        n_doc=n_doc+1
        # step 2. count the Words_count
        tottf,df,tfidf = wordcount.tot_tf(doc['raw_text'],n_doc,result_1,result_2,result_3)

    db.delete_data_from_table('totwordcount')
    db.insert_totwordcount( tottf,df,tfidf )
def figplot():
    tot_tf = db.get_data('totwordcount', 'ORDER BY tottf DESC')

    print('first 30 words per TF')
    for word in tot_tf[0:50]:
        print(word['word'],word['tottf'])
    print('---------------------------------------------------')
    plot.plot_30_words(tot_tf)

def all():
    download()
    tf()
    tot_tfdf()
    figplot()
"""


    #plot.most_200words(summary,tot_tf)
    # print main output

    #print body
    print('first 20 words per TF')
    for word in tot_tf[0:50]:
        print(word[0],word[1])
    print('---------------------------------------------------')
    print('first 20 words per DF')
    for word in df[0:50]:
        print(word[0],word[1])
    print('---------------------------------------------------')
    print('first 20 words per tfidf')
    for word in tfidf[0:50]:
        print(word[0],word[1])
"""



if __name__ =="__main__":
    argv = sys.argv
    if argv[1] == "all":
        all()

    elif argv[1] == "download":
        download()

    elif argv[1] == "tf":
        tf()

    elif argv[1] == "tot_tfdf":
        tot_tfdf()

    elif argv[1] == "figplot":
        figplot()
    else:
        print 'error!!!! no module is running'
