import requests
import unicodedata
from bs4 import BeautifulSoup
from goose import Goose

def get_data( url ):
    headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
    #result = requests.get(url,headers=headers).text
    g = Goose()
    result = g.extract(url=url)

    # trim out and get only body text
    #soup = BeautifulSoup(result, "lxml")

    body = result.cleaned_text.strip()
    title = result.title.strip()

    body = unicodedata.normalize('NFKD', body).encode('ascii','ignore')
    title = unicodedata.normalize('NFKD', title).encode('ascii','ignore')

    return title, body
