import json, requests
import time
from datetime import date, timedelta

def f1():
        url = 'http://ergast.com/api/f1/current/next.json'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        round = data['MRData']['RaceTable']['round']
        season = data['MRData']['RaceTable']['Races'][0]['season']
        wiki = data['MRData']['RaceTable']['Races'][0]['url']
        name = data['MRData']['RaceTable']['Races'][0]['raceName']
        # print(round,season,wiki,name)
        # races = data['MRData']['RaceTable']['round'][]
        # print(data['MRData']['RaceTable']['Races'][0])

def movie():
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=d1eb6d004d748e1f86bbbc2ce791b43d'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        poster = data['results'][0]['poster_path']
        vote = data['results'][0]['vote_average']
        title = data['results'][0]['title']
        overview = data['results'][0]['overview']
        print(poster, vote, title, overview)

def verge():
        url = 'https://newsapi.org/v2/top-headlines?sources=the-verge&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        author = data['articles'][0]['author']
        title = data['articles'][0]['title']
        description = data['articles'][0]['description']
        url = data['articles'][0]['url']
        image = data['articles'][0]['urlToImage']
        print(author, title, description, url, image)

def wheater():
        api= "4K2M4xKSGxA93Et2BhN4HFm9TCX07N1o"
        city = "Eindhoven"
        url = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey="+api+"&q="+city
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        citykey = data[0]['Key']
        country = data[0]['Country']['LocalizedName']
        province = data[0]["AdministrativeArea"]["LocalizedName"]
        #get the actual wheater data
        url2= "http://dataservice.accuweather.com/forecasts/v1/daily/5day/249208?apikey=4K2M4xKSGxA93Et2BhN4HFm9TCX07N1o&metric=true"
        resp = requests.get(url=url2)
        data = json.loads(resp.text)
        dailyforecasts = data['DailyForecasts']

def daily():
        url="http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        imageurl = data['images'][0]['url']
        imagelink = data['images'][0]['copyrightlink']


def stock():
        url = "https://api.iextrading.com/1.0/stock/GOOGL/quote"
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        companyname = data['companyName']
        exchange = data['primaryExchange']
        price = data['latestPrice']
        cahngepercent = data['changePercent']


stock()
# wheater()
# daily()
#f1()
# movie()
#verge()
