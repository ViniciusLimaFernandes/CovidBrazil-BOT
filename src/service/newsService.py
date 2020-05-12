from repository.news import getNews

news = getNews()
newsList = news['articles']


def getLastNews():
    try:
        lastNews = newsList[0]

        return lastNews
    except RuntimeError:
        print('List of news is empty.')


def getAllNews():
    return newsList
