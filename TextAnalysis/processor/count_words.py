import sqlite3



#import operator

##list url


## IMPORT TEXT
conn=sqlite3.connect('/home/claudia/Downloads/SQLiteStudio/obama_speaches2.db')
cur=conn.cursor()
cur.execute("DROP TABLE document")
cur.execute("DROP TABLE Words_count")

cur.execute("CREATE TABLE IF NOT EXISTS document(Id INT PRIMARY KEY, raw_text TEXT,TITLE CHAR, YEAR INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS Words_count(Id INT, word TEXT, frequency INT)")
i=-1;
for URL in URL_list:
    i=i+1
    ID=id_list[i]
    YEAR=year_list[i]
    source_code = requests.get(URL,headers=headers).text
    
    cur.execute("INSERT INTO document (Id,raw_text,TITLE,YEAR) VALUES (?,?,?,?)", (ID,main_text,title,YEAR))
    conn.commit()
    word=[]
    text_split=main_text.lower().split()
    frequency={}
    for each_word in text_split:
        count=frequency.get(each_word,0)
        frequency[each_word]=count+1

    frequency_list=frequency.keys()
    print(ID)
    for words in frequency_list:

        cur.execute("INSERT INTO Words_count VALUES (?,?,?)", (ID,words,frequency[words]))
        conn.commit()
        if frequency[words]>2:
            print words, frequency[words],ID


  #  word.append(each_word(count(text_split))
#def start(url):
#    word_list = []
#    source_code = requests.get(url).text
#    soup = BeautifulSoup(source_code)

#    for post_text in soup.findAll('a', {'class': 'index_singleListingTitles'}):
 #       content = post_text.string
 #       words = content.lower().split()
  #      print(words)
   #     for each_word in words:
    #        print(each_word)
     #       word.append(each_word)
