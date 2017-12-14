import json, requests
from .models import News



def news():
        url = 'https://newsapi.org/v2/top-headlines?sources=the-verge&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        author = data['articles'][0]['author']
        title = data['articles'][0]['title']
        description = data['articles'][0]['description']
        url = data['articles'][0]['url']
        image = data['articles'][0]['urlToImage']
        data.verge_author = author
        data.verge_title = title
        data.verge_description = description
        data.verge_url = url
        data.verge_image = image

        News.objects.create(
                news_source = source,
                news_title = title,
                news_description = description,
                news_date = date,
                news_author = author,
                news_image = image,
        )

news()
