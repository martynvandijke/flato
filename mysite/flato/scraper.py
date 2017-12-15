import json, requests
from .models import News



def news():
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
                date = article["publishedAt"]

                News.objects.create(
                        news_source = source,
                        news_title = title,
                        news_description = description,
                        news_date = date,
                        news_author = author,
                        news_image = image,
                        news_link = url,
                )

news()
