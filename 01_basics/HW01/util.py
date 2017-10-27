import requests
from bs4 import BeautifulSoup

def get_news_article(url):
    r = requests.get(url)
    #r.encoding = "UTF-8"

    soup = BeautifulSoup(r.text, "lxml")
    news_text = soup.select('div[itemprop="articleBody"]')[0].text

    return(news_text)
