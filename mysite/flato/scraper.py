import json, requests
from .models import News


def BBCnews():
        url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=25a3dde52adb4c128205ac244ee5d750'
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
                )


