from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import json, requests
from django.template import loader
from django.shortcuts import redirect
from .models import News, Movie
from django.views.generic import ListView, DetailView, TemplateView
from .scraper import GeneralNews, Movies, TechNews, ScienceNews, BusinessNews, GamingNews, SportNews , PoliticalNews
from django.db.models import Q

class MultipleModelView(TemplateView):
    template_name = 'feed.html'

    def get_context_data(self, **kwargs):
        context = super(MultipleModelView, self).get_context_data(**kwargs)
        general = self.request.user.profile.chip_general
        business = self.request.user.profile.chip_business
        politics = self.request.user.profile.chip_politics
        sport = self.request.user.profile.chip_sport
        gaming = self.request.user.profile.chip_gaming
        technology = self.request.user.profile.chip_technology

        Qgeneral = Q()
        Qbusiness = Q()
        Qpolitics = Q()
        Qsport = Q()
        Qgaming = Q()
        Qtechnology = Q()
        Qtitle = Q()
        Qauthor = Q()
        Qnewsnumber = 10
        Qdescription = Q()
        Qtime = Q()
        if self.request.session['newsnumber']:
            Qnewsnumber = self.request.session['newsnumber']
        else:
            Qnewsnumber = 20

        if self.request.session['title']:
            Qtitle = Q(title=str(self.request.session['title']))
            print(Qtitle)

        if self.request.session['description']:
            Qdescription = Q(description=self.request.session['description'])

        if self.request.session['author']:
            Qauthor = Q(author=self.request.session['author'] )

        if self.request.session['time']:
            Qtime = Q(time=self.request.session['time'])


        if general == "True":
            Qgeneral = Q(tag="General")
            print("gen")
        if business == "True":
            Qbusiness = Q(tag="Business")
            print("bus")
        if politics == "True":
            Qpolitics = Q(tag="Politics")
            print("poli")
        if sport == "True":
            Qsport = Q(tag="Sport")
            print("sport")
        if gaming == "True":
            Qgaming = Q(tag="Gaming")
            print("gaming")
        if technology == "True":
            Qtechnology = Q(tag="Technology ")
            print("tec")
        print(        Qgeneral,
        Qbusiness,
        Qpolitics,
        Qsport,
        Qgaming,
        Qtechnology,
        Qtitle,
)
        context['newslist'] = News.objects.filter(

        Qgeneral|
        Qbusiness|
        Qpolitics|
        Qsport|
        Qgaming|
        Qtechnology|
        Qtitle


        ).order_by("-date")[:int(Qnewsnumber)]
        # context['movielist'] = Movie.objects.all().order_by("-popularity")[:9]
        context['general'] = self.request.user.profile.chip_general
        context['business'] = self.request.user.profile.chip_business
        context['politics'] = self.request.user.profile.chip_politics
        context['sport'] = self.request.user.profile.chip_sport
        context['gaming'] = self.request.user.profile.chip_gaming
        context['technology'] = self.request.user.profile.chip_technology
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie.html'

def addchip(request):
        user = User.objects.get(pk=request.user.id)
        data = request.GET.get('chip', None)
        if data.lower() == "general":
            user.profile.chip_general = "True"
        if data.lower() == "business":
            user.profile.chip_business = "True"
        if data.lower() == "politics":
            user.profile.chip_politics = "True"
        if data.lower() == "sport":
            user.profile.chip_sport = "True"
        if data.lower() == "gaming":
            user.profile.chip_gaming = "True"
        if data.lower() == "technology":
            user.profile.chip_technology = "True"

        user.save()
        print("adding")
        return redirect('/feed', permanent=True)

def deletechip(request):
        user = User.objects.get(pk=request.user.id)
        data = request.GET.get('chip', None)
        if data.lower() == "general":
            user.profile.chip_general = "False"
        if data.lower() == "business":
            user.profile.chip_business = "False"
        if data.lower() == "politics":
            user.profile.chip_politics = "False"
        if data.lower() == "sport":
            user.profile.chip_sport = "False"
        if data.lower() == "gaming":
            user.profile.chip_gaming = "False"
        if data.lower() == "technology":
            user.profile.chip_technology = "False"

        user.save()
        print("tesdsfsd")
        return redirect('/feed', permanent=True)


def search(request):
    if request.method == 'POST':
        newsnumber = request.POST.get("newsnumber")
        title  = request.POST.get("title")
        description = request.POST.get("description")
        author = request.POST.get("author")
        time = request.POST.get("time")
        request.session['newsnumber'] = newsnumber
        request.session['title'] = title
        request.session['description'] = description
        request.session['author'] = author
        request.session['time'] = time

        print(newsnumber,title, description, author, time)
        return redirect ('/feed')



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
    GamingNews()
    SportNews()
    PoliticalNews()

    return HttpResponse("updated BBCnews and Movies ")