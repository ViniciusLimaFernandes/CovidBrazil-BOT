import time
from twitter.service.twitterService import postActualStatus, postLastNews

print('Starting application...')

while True:
    postActualStatus()
    time.sleep(120)
    postLastNews()
    time.sleep(7200)
