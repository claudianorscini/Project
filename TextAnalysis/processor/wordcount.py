import string
import operator as op
import unicodedata
from nltk.corpus import stopwords
translation_table = string.maketrans(string.punctuation+string.digits+string.uppercase,
                                 " "*len(string.punctuation+string.digits)+string.lowercase)

def clean_data(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    text_clean = text.translate(translation_table)
    return text_clean

def filter_common_words(word_list):
    s = set(stopwords.words('english'))
    line_filter = filter(lambda w: not w in s,word_list)
    return line_filter



def tf(text):

    result = {}
    result2 = {}
    text_clean = clean_data(text)
    text_filt=filter_common_words(text_clean.split())
    numb_words=len(text_filt)
    print numb_words
    for each_word in text_filt:
        if result.get(each_word):
            result[each_word] = result[each_word] + 1
            result2[each_word] = result[each_word]*1./numb_words
        else:
            result[each_word] = 1
            result2[each_word] = result[each_word]*1./numb_words
    return result,result2


def tot_tf(text,n_doc,tottf,df,tfidf):
    text_clean = clean_data(text)

    text_filt = filter_common_words(text_clean.split())
    numb_words=len(text_filt)
    #print numb_words

    for each_word in text_filt:
        if tottf.get(each_word):
            tottf[each_word] = tottf[each_word] + 1

            if df[each_word] != n_doc:

                    df[each_word]=df[each_word]+1
                    tfidf[each_word]=tottf[each_word]/df[each_word]
            else:
                    df[each_word]=df[each_word]
                    tfidf[each_word]=tottf[each_word]/df[each_word]

        else:
            tottf[each_word] = 1
            df[each_word] = 1
            tfidf[each_word]=tottf[each_word]/df[each_word]

    return tottf,df,tfidf



            
