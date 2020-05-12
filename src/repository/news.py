import requests
from utils.tools import AuthData

credentials = AuthData.oauthData()
apiKey = credentials.newsApi_key
domains = "uol.com.br,globo.com,ig.com.br,www.jn.pt"

req = requests.get(
    f'https://newsapi.org/v2/everything?qInTitle=Covid-19&domains={domains}&sortBy=publishedAt&pageSize=10&apiKey={apiKey}')
news = req.json()


def getNews():
    return news
