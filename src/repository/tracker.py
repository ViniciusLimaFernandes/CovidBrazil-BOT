import requests

onlyBrazilURL =  "https://covid19-brazil-api.now.sh/api/report/v1/brazil"

req = requests.get(onlyBrazilURL)
data = req.json()

def getCovidData():
    return data
