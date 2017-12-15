from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import json, requests
from django.template import loader
from django.shortcuts import redirect
from .models import News
from django.views.generic import ListView, DeleteView


class NewsList(DeleteView):
    model = News
    template_name = 'news.html'


def index(request):



    if request.user.is_authenticated():
                template = loader.get_template('index.html')
                print( News.objects.values_list('news_title',flat=True))
                context = {
                    "news": News.objects.all(),
                    'titles': News.objects.values_list('news_title',flat=True),
                    'sources': News.objects.values_list('news_source',flat=True),
                    'descriptions': News.objects.values_list('news_description',flat=True),
                    'dates': News.objects.values_list('news_date', flat=True),
                    'authors': News.objects.values_list('news_author', flat=True),

                }
                return HttpResponse(template.render(context, request))

    else:
        return redirect('/login/')

def update(request):

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
            date = article["publishedAt"]
            News.objects.create(
                news_source=source,
                news_title=title,
                news_description=description,
                news_date=date,
                news_author=author,
                news_image=image,
                news_link=url,
            )


    BBCnews()
    return HttpResponse("updated BBCnews")