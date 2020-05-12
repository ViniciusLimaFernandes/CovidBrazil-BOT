from repository.tracker import getCovidData


class TrackerService:
    def __init__(self, numOfSuspects, numOfConfirmed, numOfDeaths, numOfRecovered, updatedAt):
        self.numOfSuspects = numOfSuspects
        self.numOfConfirmed = numOfConfirmed
        self.numOfDeaths = numOfDeaths
        self.numOfRecovered = numOfRecovered
        self.updatedAt = updatedAt

    def covidData():
        print('Parsing API data...')

        data = getCovidData()
        dataPath = data['data']
        response = TrackerService(
            dataPath['cases'], dataPath['confirmed'], dataPath['deaths'], dataPath['recovered'], dataPath['updated_at'])

        print(f'Got response = {data}')

        return response
