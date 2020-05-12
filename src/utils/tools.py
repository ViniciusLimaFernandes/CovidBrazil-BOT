import json
import datetime
from pytz import timezone


class AuthData:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, newsApi_key):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.newsApi_key = newsApi_key

    def oauthData():
        print('c=AuthData m=oauthData message=Parsing json with credentials...')
        with open('./user/credentials.json') as json_file:
            data = json.load(json_file)

            credentials = AuthData(data["consumer_key"], data["consumer_secret"],
                                   data["access_token"], data["access_token_secret"], data["newsApi_key"])

            return credentials


def formatDatePost(date):
    now = datetime.datetime.now()
    fuse = timezone('America/Sao_Paulo')
    now = now.astimezone(fuse)
    date = date.replace("T", " ")
    date = date.replace("Z", "")
    date_time_obj = datetime.datetime.strptime(
        date, '%Y-%m-%d %H:%M:%S.%f')

    srtDate = str(date_time_obj)
    year = srtDate.split('-')[0]
    mouth = srtDate.split('-')[1]
    day = (srtDate.split('-')[2]).split(" ")[0]
    hour = now.strftime("%H:%M:%S")

    formatedDate = f'{day}/{mouth}/{year} às {hour}'

    return formatedDate
