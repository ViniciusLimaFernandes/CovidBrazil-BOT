from repository.news import getNews

news = getNews()
newsList = news['articles']


def getLastNews():
    try:
        lastNews = newsList[0]

        return lastNews
    except RuntimeError:
        print('No news available at this time')


def getAllNews():
    return newsList
