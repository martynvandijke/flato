from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import json, requests
from django.template import loader
from django.shortcuts import redirect
from .models import News, Movie
from django.views.generic import ListView, DetailView, TemplateView
from .scraper import GeneralNews, Movies, TechNews, ScienceNews, BusinessNews
from time import  timezone

class MultipleModelView(TemplateView):
    template_name = 'feed.html'
    def get_context_data(self, **kwargs):
        context = super(MultipleModelView, self).get_context_data(**kwargs)
        context['newslist'] = News.objects.filter().order_by("-date")[:10]
        # context['movielist'] = Movie.objects.all().order_by("-popularity")[:9]

        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie.html'


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

    try:
        GeneralNews()
    except:
        print("BBC News Error")

    try:
        Movies()
    except:
        print("error")
    BusinessNews()
    TechNews()
    ScienceNews()

    return HttpResponse("updated BBCnews and Movies ")