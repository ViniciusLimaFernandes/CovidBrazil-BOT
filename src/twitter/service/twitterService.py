from service.trackerService import TrackerService
from twitter.twitterInteractions import postTweetMessage
from service.newsService import *
from utils.tools import *


def postActualStatus():
    data = TrackerService.covidData()

    numOfSuspects = data.numOfSuspects
    numOfConfirmed = data.numOfConfirmed
    numOfDeaths = data.numOfDeaths
    numOfRecovered = data.numOfRecovered
    updatedAt = data.updatedAt

    date = formatDatePost(updatedAt)

    message = f"🇧🇷 Brasil 🇧🇷 : \n\n⚠️ Numero de suspeitas: {numOfSuspects}\n☢️ Casos confirmados: {numOfConfirmed}\n🪦 Numero de mortes: {numOfDeaths}\n🚑 Recuperados: {numOfRecovered}\n---------------------------------------\nÚltima atualização {date}\n\n#covid19 #coronavirus #covid19brasil #FiqueEmCasa #FicaEmCasa"

    print(f'm=postActualStatus message=Message builded = {message}')

    postTweetMessage(message)

    print("m=postActualStatus message=Message posted! check at: https://twitter.com/CovidBrazil")


def postLastNews():
    lastNews = getLastNews()
    title = lastNews['title']
    newsUrl = lastNews['url']
    postTime = lastNews['publishedAt']

    message = f'📃 Notícia 📃 : \n\n 📡 {title}\n\nDisponível em: {newsUrl}\n\n #covid19 #coronavirus #covid19brasil #FiqueEmCasa #FicaEmCasa'

    print(f'm=postLastNews message=Message builded = {message}')

    try:
        postTweetMessage(message)

        print("m=postLastNews message=Message posted! check at: https://twitter.com/CovidBrazil")
    except Exception as e:
        print(f'\n[WARN] m=postLastNews message=Caught exception {e}')
        print(
            f'[WARN] m=postLastNews message=Message not posted, its duplicated\n')
