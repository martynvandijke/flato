from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import json, requests
from django.template import loader
from django.shortcuts import redirect
from .models import News
from django.views.generic import ListView, DetailView
from .scraper import BBCnews

class NewsListView(ListView):
    model = News
    queryset = News.objects.order_by("-date")[:9]

    template_name = 'feed.html'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news.html'

def index(request):

    if request.user.is_authenticated():
                template = loader.get_template('index.html')
                context = {
                    'images' : "[test,fsdfseff]"
                }
                return HttpResponse(template.render(context, request))

    else:
        return redirect('/login/')

def update(request):
    BBCnews()

    # try:
    #     BBCnews()
    # except:
    #     print("BBC News Error")

    return HttpResponse("updated BBCnews")