import json, requests, datetime
from .models import News, Movie


def GeneralNews():
        url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news,google-news,reuters,reddit-r-all,rtl-nieuws,the-telegraph&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        articles = data['articles']
        for article in articles:
                source = article['source']['name']
                author = article['author']
                title = article['title']
                description = article['description']
                url = article['url']
                image = article['urlToImage']
                dateFull = article["publishedAt"]
                temp = dateFull.split('T')
                date = temp[0]
                time = temp[1].split("Z")
                time = time[0]
                News.objects.create(
                        source=source,
                        title=title,
                        description=description,
                        date=date,
                        time=time,
                        author=author,
                        image=image,
                        link=url,
                        tag="General"
                )


def TechNews():
        url = 'https://newsapi.org/v2/top-headlines?sources=crypto-coins-news,the-verge,wired&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        articles = data['articles']
        for article in articles:
                source = article['source']['name']
                author = article['author']
                title = article['title']
                description = article['description']
                url = article['url']
                image = article['urlToImage']
                dateFull = article["publishedAt"]
                temp = dateFull.split('T')
                date = temp[0]
                time = temp[1].split("Z")
                time = time[0]
                News.objects.create(
                        source=source,
                        title=title,
                        description=description,
                        date=date,
                        time=time,
                        author=author,
                        image=image,
                        link=url,
                        tag="Technology"
                )


def ScienceNews():
        url = 'https://newsapi.org/v2/top-headlines?sources=new-scientist,national-geographic&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        articles = data['articles']
        for article in articles:
                source = article['source']['name']
                author = article['author']
                title = article['title']
                description = article['description']
                url = article['url']
                image = article['urlToImage']
                dateFull = article["publishedAt"]
                temp = dateFull.split('T')
                date = temp[0]
                time = temp[1].split("Z")
                time = time[0]
                News.objects.create(
                        source=source,
                        title=title,
                        description=description,
                        date=date,
                        time=time,
                        author=author,
                        image=image,
                        link=url,
                        tag="Science and nature"
                )


def BusinessNews():
        url = 'https://newsapi.org/v2/top-headlines?sources=bloomberg,cnbc,business-insider-uk,cbs-news&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        articles = data['articles']
        for article in articles:
                source = article['source']['name']
                author = article['author']
                title = article['title']
                description = article['description']
                url = article['url']
                image = article['urlToImage']
                dateFull = article["publishedAt"]
                temp = dateFull.split('T')
                date = temp[0]
                time = temp[1].split("Z")
                time = time[0]
                News.objects.create(
                        source=source,
                        title=title,
                        description=description,
                        date=date,
                        time=time,
                        author=author,
                        image=image,
                        link=url,
                        tag="Business"
                )


def PoliticalNews():
        url = 'https://newsapi.org/v2/top-headlines?sources=politico,the-hill,breitbart-news&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        articles = data['articles']
        for article in articles:
                source = article['source']['name']
                author = article['author']
                title = article['title']
                description = article['description']
                url = article['url']
                image = article['urlToImage']
                dateFull = article["publishedAt"]
                try:
                        temp = dateFull.split('T')
                        date = temp[0]
                        time = temp[1].split("Z")
                        time = time[0]
                except:
                        time=datetime.datetime.now().time()
                        date=datetime.datetime.now()
                News.objects.create(
                        source=source,
                        title=title,
                        description=description,
                        date=date,
                        time=time,
                        author=author,
                        image=image,
                        link=url,
                        tag="Politics"
                )


def SportNews():
        url = 'https://newsapi.org/v2/top-headlines?sources=espn,bbc-sport,nhl-news&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        articles = data['articles']
        for article in articles:
                source = article['source']['name']
                author = article['author']
                title = article['title']
                description = article['description']
                url = article['url']
                image = article['urlToImage']
                dateFull = article["publishedAt"]
                try:
                        temp = dateFull.split('T')
                        date = temp[0]
                        time = temp[1].split("Z")
                        time = time[0]
                except:
                        time=datetime.datetime.now().time()
                        date=datetime.datetime.now()
                News.objects.create(
                        source=source,
                        title=title,
                        description=description,
                        date=date,
                        time=time,
                        author=author,
                        image=image,
                        link=url,
                        tag="Sport"
                )

def GamingNews():
        url = 'https://newsapi.org/v2/top-headlines?sources=polygon&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        articles = data['articles']
        for article in articles:
                source = article['source']['name']
                author = article['author']
                title = article['title']
                description = article['description']
                url = article['url']
                image = article['urlToImage']
                dateFull = article["publishedAt"]
                temp = dateFull.split('T')
                date = temp[0]
                time = temp[1].split("Z")
                time = time[0]
                News.objects.create(
                        source=source,
                        title=title,
                        description=description,
                        date=date,
                        time=time,
                        author=author,
                        image=image,
                        link=url,
                        tag="Gaming"
                )

def Movies():
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=d1eb6d004d748e1f86bbbc2ce791b43d'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        results = data['results']
        for result in results:
                poster_path = result['poster_path']
                vote_average = result['vote_average']
                vote_count = result['vote_count']
                title = result['title']
                overview = result['overview']
                backdrop_path = result['backdrop_path']
                gerne_ids = result['genre_ids']
                popularity = result['popularity']
                date = result['release_date']
                Movie.objects.create(
                        title=title,
                        vote_count=vote_count,
                        vote_average=vote_average,
                        overview=overview,
                        backdrop_path=backdrop_path,
                        poster_path=poster_path,
                        gerne_ids=gerne_ids,
                        date=date,
                        popularity=popularity
                )


