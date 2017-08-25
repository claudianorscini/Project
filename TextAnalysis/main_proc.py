import db.db_proc as db
import processor.download as download
import processor.wordcount as wordcount
import plot.plots as plot
#import plot.plot as plot
import numpy as np
# fetch url from the db
urls = db.get_doc_urls()
summary=[]
for url in urls[0:1]:
    # step 1. download the raw text
    title, body = download.download_raw_text(url['URL'])
    db.save_raw_text( url['id'], title, body )

    # step 2. count the Words_count
    tf,numb_words = wordcount.tf(body)
    db.delete_term_freq( url['id'] )
    db.insert_term_freq( url['id'], tf )

#step 3. save total frequency and document frequency to calcculate relevance
    summary = wordcount.make_total_summary(tf,url,summary,numb_words)
tottf,df,tfidf = wordcount.calculate_tot_tf_df(summary)


db.insert_global_data(tottf)
db.insert_global_data(df)
db.insert_global_data(tfidf)



# step 4. save the data in DB
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
