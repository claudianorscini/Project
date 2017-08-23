import facebook    #sudo pip install facebook-sdk
import itertools
import json
import re
import requests
import operator
from matplotlib import style
import pandas as pd
# Adjusting the size of matplotlib
import matplotlib.pylab as mpl
import matplotlib.dates as dates
access_token = "EAAEzbQrbBFMBAOayNnraoTTywOz6Pzi7kRI9CzbZAzZByZCab68EY6adZC85p5kvWXJJKBCqmE51ExwmEQnVWlii1puKHMIn941JEw655mOFkG84oMyWdKfrxkZB851d0pwWmgQimEt4XlgMlEvCxqZBYQMfwCKkQA61v0Ld0ZA8AZDZD"
user = 'iGuzziniOfficial'
user = 'tods'


graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts', limit = 100,offset =2)
posts1 = graph.get_connections(profile['id'], 'posts', limit = 100,offset =100)
posts2 = graph.get_connections(profile['id'], 'posts', limit = 100,offset =200)
posts3 = graph.get_connections(profile['id'], 'posts', limit = 100,offset =300)
posts4 = graph.get_connections(profile['id'], 'posts', limit = 100,offset =400)
posts5 = graph.get_connections(profile['id'], 'posts', limit = 100,offset =500)
posts6 = graph.get_connections(profile['id'], 'posts', limit = 100,offset =600)
posts7 = graph.get_connections(profile['id'], 'posts', limit = 100,offset =700)
posts8 = graph.get_connections(profile['id'], 'posts', limit = 100,offset =800)
posts9 = graph.get_connections(profile['id'], 'posts', limit = 100,offset =900)
Posts = posts['data'] #+posts1 ['data']+ posts2['data'] +posts3['data']+posts4['data']+posts5['data']+posts6['data']+posts7['data']+posts8['data']+posts9['data']
print len(Posts)
totrate=[]
albumrate = []
it=-1
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

style.use('ggplot')

#fig, ax = mpl.subplots()
it_album = -1
tot_comments = 0
tot_likes = 0
tot_shares = 0
for i in Posts:
    allID = i['id']
    Postinfo =  graph.request(path=allID)

    #print i
    try:

        if 'story' in Postinfo.keys():
            print 'album'
            print it_album
            it_album = it_album+1
            alllikes = graph.get_connections(id = allID,connection_name = 'likes',summary = 'true'  )
            allComments =  graph.get_connections(id = allID,connection_name = 'comments',summary = 'true'  )
            allshare =  graph.request(path=allID,args={'fields':'shares'})
            n_likes = alllikes['summary']['total_count']
            n_comments = allComments['summary']['total_count']

            if 'shares' in allshare.keys():

                n_shares = allshare['shares']['count']
            else:
                n_shares = 0

            albumrate.append({'id':allID,'time':created_time, 'lik':n_likes,'sha': n_shares, 'com' :n_comments})


        else :
            print 'single post'
            it = it+1
            print it
            created_time =i['created_time']

            allComments =  graph.get_connections(id = allID,connection_name = 'comments',summary = 'true'  )
            allshare =  graph.request(path=allID,args={'fields':'shares'})
            alllikes = graph.get_connections(id = allID,connection_name = 'likes',summary = 'true'  )
            #allshare =  graph.get_connections(id = allID,connection_name = 'shares',summary = 'true'  )
            n_likes = alllikes['summary']['total_count']
            tot_likes = tot_likes + n_likes
            n_comments = allComments['summary']['total_count']
            tot_comments = tot_comments + n_comments
            if 'shares' in allshare.keys():

                n_shares = allshare['shares']['count']
                tot_shares = tot_shares + n_shares

            else:
                n_shares = 0

            totrate.append({'id':allID,'time':created_time, 'lik':n_likes*1./tot_likes,'sha': n_shares*1./tot_shares, 'com' :n_comments*1./tot_comments})

        #print it
        time = totrate[it]['time']
        xvalue = (str(time[0:10]).replace('-',''))

        new_x = dates.datestr2num(xvalue)
        mpl.plot_date(new_x,totrate[it]['lik'],'bo', xdate = True)
        mpl.plot_date(new_x,totrate[it]['sha'],'ro',xdate = True)
        mpl.plot_date(new_x,totrate[it]['com'],'ko',xdate = True)



    except (UnicodeEncodeError):
        pass
newlist = sorted(totrate, key = lambda k : k['lik'],reverse = True)

for i in range(50):
    id_max = newlist[i]['id']
    Post_max =  graph.request(path=id_max)
    print Post_max
    print newlist[i]
mpl.show()

    # Adjusting the style of matpl
