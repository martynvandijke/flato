from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.models import User
import json, requests
from .models import Data
from datetime import datetime, timedelta


def getdata(request):

    def f1():
        url = 'http://ergast.com/api/f1/current/next.json'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        round = data['MRData']['RaceTable']['round']
        season = data['MRData']['RaceTable']['Races'][0]['season']
        wiki = data['MRData']['RaceTable']['Races'][0]['url']
        name = data['MRData']['RaceTable']['Races'][0]['raceName']
        date = data['MRData']['RaceTable']['Races'][0]['date']
        time = data['MRData']['RaceTable']['Races'][0]['time']
        data = Data.objects.get(pk=1)
        data.f1_round = round
        data.f1_season = season
        data.f1_wiki = wiki
        data.f1_name = name
        data.f1_date = date
        data.f1_time = time
        data.save()


    def movie():
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=d1eb6d004d748e1f86bbbc2ce791b43d'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        poster = data['results'][0]['poster_path']
        vote = data['results'][0]['vote_average']
        title = data['results'][0]['title']
        overview = data['results'][0]['overview']
        data = Data.objects.get(pk=1)
        data.movie_poster = poster
        data.movie_vote = vote
        data.movie_title = title
        data.movie_overview = overview
        data.save()


    def verge():
        url = 'https://newsapi.org/v2/top-headlines?sources=the-verge&apiKey=25a3dde52adb4c128205ac244ee5d750'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        author = data['articles'][0]['author']
        title = data['articles'][0]['title']
        description = data['articles'][0]['description']
        url = data['articles'][0]['url']
        image = data['articles'][0]['urlToImage']
        data = Data.objects.get(pk=1)
        data.verge_author = author
        data.verge_title = title
        data.verge_description = description
        data.verge_url = url
        data.verge_image = image
        data.save()

    def wheater():
        api = "4K2M4xKSGxA93Et2BhN4HFm9TCX07N1o"
        city = request.user.profile.wheater_city
        url = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=" + api + "&q=" + city
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        citykey = data[0]['Key']
        country = data[0]['Country']['LocalizedName']
        province = data[0]["AdministrativeArea"]["LocalizedName"]
        # current wheater
        url3 = "http://dataservice.accuweather.com/currentconditions/v1/"+citykey+"?apikey=4K2M4xKSGxA93Et2BhN4HFm9TCX07N1o&metric=true"
        resp = requests.get(url=url3)
        data = json.loads(resp.text)
        today = data[0]['Temperature']['Metric']['Value']

        ## get forecast
        url2 = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"+citykey+"?apikey=4K2M4xKSGxA93Et2BhN4HFm9TCX07N1o&metric=true"
        resp = requests.get(url=url2)
        data = json.loads(resp.text)
        dailyforecasts = data['DailyForecasts']
        # print(dailyforecasts)
        day1_min = dailyforecasts[0]["Temperature"]["Minimum"]['Value']
        day1_max = dailyforecasts[0]["Temperature"]["Maximum"]['Value']
        day1_icon = dailyforecasts[0]["Day"]["Icon"]
        day2_min = dailyforecasts[1]["Temperature"]["Minimum"]['Value']
        day2_max = dailyforecasts[1]["Temperature"]["Maximum"]['Value']
        day2_icon = dailyforecasts[1]["Day"]["Icon"]
        day3_min = dailyforecasts[2]["Temperature"]["Minimum"]['Value']
        day3_max = dailyforecasts[2]["Temperature"]["Maximum"]['Value']
        day3_icon = dailyforecasts[2]["Day"]["Icon"]
        day4_min = dailyforecasts[3]["Temperature"]["Minimum"]['Value']
        day4_max = dailyforecasts[3]["Temperature"]["Maximum"]['Value']
        day4_icon = dailyforecasts[3]["Day"]["Icon"]
        day5_min = dailyforecasts[4]["Temperature"]["Minimum"]['Value']
        day5_max = dailyforecasts[4]["Temperature"]["Maximum"]['Value']
        day5_icon = dailyforecasts[4]["Day"]["Icon"]

        data = Data.objects.get(pk=1)
        data.wheater_cirtykey = citykey
        data.wheater_country = country
        data.wheater_province = province
        data.wheater_dailyforecasts = dailyforecasts
        data.wheater_today = today
        data.wheater_day1_min = day1_min
        data.wheater_day1_max = day1_max
        data.wheater_day1_icon = day1_icon
        data.wheater_day2_min = day2_min
        data.wheater_day2_max = day2_max
        data.wheater_day2_icon = day2_icon
        data.wheater_day3_min = day3_min
        data.wheater_day3_max = day3_max
        data.wheater_day3_icon = day3_icon
        data.wheater_day4_min = day4_min
        data.wheater_day4_max = day4_max
        data.wheater_day4_icon = day4_icon
        data.wheater_day5_min = day5_min
        data.wheater_day5_max = day5_max
        data.wheater_day5_icon = day5_icon

        data.save()



    def daily():
        url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        imageurl = data['images'][0]['url']
        imagelink = data['images'][0]['copyrightlink']
        data = Data.objects.get(pk=1)
        data.daily_imageurl = imageurl
        data.daily_imagelink = imagelink
        data.save()


    def stock():
        url = "https://api.iextrading.com/1.0/stock/GOOGL/quote"
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        companyname = data['companyName']
        exchange = data['primaryExchange']
        price = data['latestPrice']
        cahngepercent = data['changePercent']
        data = Data.objects.get(pk=1)
        data.stock_companyname = companyname
        data.stock_exchange = exchange
        data.stock_price = price
        data.stock_changepercent = cahngepercent
        data.save()


    try:
        f1()
        request.session['f1'] = True
    except:
        print("f1 error")
        request.session['f1'] = False

    try:
        wheater()
        request.session['wheater'] = True

    except:
        print("wheater error")
        request.session['wheater'] = False


    try:
        verge()
        request.session['verge'] = True

    except:
        print("verge error")
        request.session['verge'] = False

    try:
        daily()
        request.session['daily'] = True

    except:
        print("daily error")
        request.session['daily'] = False


    try:
        movie()
        request.session['movie'] = True

    except:
        print("movie error")
        request.session['movie'] = False

    try:
        stock()
        request.session['stock'] = True

    except:
        print("stock error")
        request.session['stock'] = False


def index(request):

    if request.user.is_authenticated():

        if request.session.get('updatedb'):
            if request.session['updatedb'] == True:
                request.session['updatedb'] = False

                if request.session['f1'] == True:
                    f1 = True
                else:
                    f1 = False
                if request.session['wheater'] == True:
                    wheater = True
                else:
                    wheater = False
                if request.session['verge'] == True:
                    verge = True
                else:
                    verge = False
                if request.session['daily'] == True:
                    daily = True
                else:
                    daily = False
                if request.session['stock'] == True:
                    stock = True
                else:
                    stock = False
                if request.session['movie'] == True:
                    movie = True
                else:
                    movie = False
                print(f1)
                template = loader.get_template('index.html')
                data = Data.objects.get(pk=1)
                context = {
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'user_name': request.user.username,
                    'room_status': request.user.profile.room_status,
                    'wheater_satus': request.user.profile.wheater_satus,
                    'daily_status': request.user.profile.daily_status,
                    'verge_status': request.user.profile.verge_status,
                    'stock_status': request.user.profile.stock_status,
                    'movie_status': request.user.profile.movie_status,
                    'f1_status': request.user.profile.f1_status,
                    'f1_name': data.f1_name,
                    'f1_round': data.f1_round,
                    'f1_season': data.f1_season,
                    'f1_wiki': data.f1_wiki,
                    'movie_poster': data.movie_poster,
                    'movie_vote': data.movie_vote,
                    'movie_title': data.movie_title,
                    'movie_overview': data.movie_overview,
                    'verge_author': data.verge_author,
                    'verge_title': data.verge_title,
                    'verge_description': data.verge_description,
                    'verge_url': data.verge_url,
                    'verge_image': data.verge_image,
                    'wheater_country': data.wheater_country,
                    'wheater_province': data.wheater_province,
                    'wheater_daily': data.wheater_dailyforecasts,
                    'wheater_city': request.user.profile.wheater_city,
                    'wheater_degree': request.user.profile.wheater_degree,
                    'wheater_today' : data.wheater_today,
                    'wheater_day1_min' : data.wheater_day1_min,
                    'wheater_day1_max' : data.wheater_day1_max,
                    'wheater_day1_icon' : data.wheater_day1_icon,
                    'wheater_day2_min' : data.wheater_day2_min,
                    'wheater_day2_max' : data.wheater_day2_max,
                    'wheater_day2_icon' : data.wheater_day2_icon,
                    'wheater_day3_min' : data.wheater_day3_min,
                    'wheater_day3_max' : data.wheater_day3_max,
                    'wheater_day3_icon' : data.wheater_day3_icon,
                    'wheater_day4_min' : data.wheater_day4_min,
                    'wheater_day4_max' : data.wheater_day4_max,
                    'wheater_day4_icon' : data.wheater_day4_icon,
                    'wheater_day5_min' : data.wheater_day5_min,
                    'wheater_day5_min' : data.wheater_day5_max,
                    'wheater_day5_icon' : data.wheater_day5_icon,
                    'daily_url': data.daily_imageurl,
                    'dailt_link': data.daily_imagelink,
                    'stock_companyname': data.stock_companyname,
                    'stock_excahnge': data.stock_exchange,
                    'stock_price': data.stock_price,
                    'stock_changepercent': data.stock_changepercent,
                    'updatedb': "yes",
                    'f1': f1,
                    'wheater': wheater,
                    'verge': verge,
                    'daily': daily,
                    'movie': movie,
                    'stock' :stock,
                    'day2' : (datetime.utcnow() + timedelta(days=1)).strftime("%A"),
                    'day3': (datetime.utcnow() + timedelta(days=2)).strftime("%A")

                }
                return HttpResponse(template.render(context, request))

        else :
            request.session['updatedb'] = False
            template = loader.get_template('index.html')
            data = Data.objects.get(pk=1)
            context ={
                'first_name' : request.user.first_name,
                'last_name': request.user.last_name,
                'user_name' : request.user.username,
                'room_status' : request.user.profile.room_status,
                'wheater_satus' : request.user.profile.wheater_satus,
                'daily_status' : request.user.profile.daily_status,
                'verge_status' : request.user.profile.verge_status,
                'stock_status' : request.user.profile.stock_status,
                'movie_status' : request.user.profile.movie_status,
                'f1_status' : request.user.profile.f1_status,
                'f1_name' : data.f1_name,
                'f1_round' : data.f1_round,
                'f1_season' : data.f1_season,
                'f1_wiki' : data.f1_wiki,
                'f1_date' : data.f1_date,
                'f1_time': data.f1_time,
                'movie_poster' : data.movie_poster,
                'movie_vote' : data.movie_vote,
                'movie_title' : data.movie_title,
                'movie_overview' : data.movie_overview,
                'verge_author' : data.verge_author,
                'verge_title' : data.verge_title,
                'verge_description' : data.verge_description,
                'verge_url' : data.verge_url,
                'verge_image' : data.verge_image,
                'wheater_country' : data.wheater_country,
                'wheater_province' : data.wheater_province,
                'wheater_daily' : data.wheater_dailyforecasts,
                'wheater_city': request.user.profile.wheater_city,
                'wheater_degree': request.user.profile.wheater_degree,
                'wheater_today': data.wheater_today,
                'wheater_day1_min': data.wheater_day1_min,
                'wheater_day1_max': data.wheater_day1_max,
                'wheater_day1_icon': data.wheater_day1_icon,
                'wheater_day2_min': data.wheater_day2_min,
                'wheater_day2_max': data.wheater_day2_max,
                'wheater_day2_icon': data.wheater_day2_icon,
                'wheater_day3_min': data.wheater_day3_min,
                'wheater_day3_max': data.wheater_day3_max,
                'wheater_day3_icon': data.wheater_day3_icon,
                'wheater_day4_min': data.wheater_day4_min,
                'wheater_day4_max': data.wheater_day4_max,
                'wheater_day4_icon': data.wheater_day4_icon,
                'wheater_day5_min': data.wheater_day5_min,
                'wheater_day5_min': data.wheater_day5_max,
                'wheater_day5_icon': data.wheater_day5_icon,
                'daily_url' : data.daily_imageurl,
                'dailt_link' : data.daily_imagelink,
                'stock_companyname' :data.stock_companyname,
                'stock_excahnge' : data.stock_exchange,
                'stock_price' : data.stock_price,
                'stock_changepercent' : data.stock_changepercent,
                'day2': (datetime.utcnow() + timedelta(days=1)).strftime("%A"),
                'day3': (datetime.utcnow() + timedelta(days=2)).strftime("%A")

            }
            return HttpResponse(template.render(context, request))

    else:
        return redirect('/login/')


def force(request):
    getdata()
    return HttpResponse("updated db")

def updatedb(request):
    getdata(request)
    request.session['updatedb'] =True
    return redirect('/')

def wheater(request):
    if request.method == 'POST':
        city = request.POST.get("city")
        user = User.objects.get(pk=request.user.id)
        user.profile.wheater_city = city
        user.save()
    return redirect('/')


def update(request):
    if request.method == 'POST':
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        user_name =  request.POST.get("username")
        user = User.objects.get(pk=request.user.id)
        user.first_name = first_name
        user.last_name = last_name
        user.username =user_name
        user.save()
    return redirect('/')

def updatewheater(request):
    user = User.objects.get(pk=request.user.id)
    data = request.GET.get('wheater', None)
    user.profile.wheater_status = data
    user.save()
    return HttpResponse("saved")

def updateroom(request):
    user = User.objects.get(pk=request.user.id)
    data = request.GET.get('room', None)
    user.profile.room_status = data
    user.save()
    return HttpResponse("saved")

def updatestock(request):
    user = User.objects.get(pk=request.user.id)
    data = request.GET.get('stock', None)
    user.profile.stock_status = data
    user.save()
    return HttpResponse("saved")

def updatedaily(request):
    user = User.objects.get(pk=request.user.id)
    data = request.GET.get('daily', None)
    user.profile.daily_status = data
    user.save()
    return HttpResponse("saved")

def updatemovie(request):
    user = User.objects.get(pk=request.user.id)
    data = request.GET.get('movie', None)
    user.profile.movie_status = data
    user.save()
    return HttpResponse("saved")

def updateverge(request):
    user = User.objects.get(pk=request.user.id)
    data = request.GET.get('verge', None)
    user.profile.verge_status = data
    user.save()
    return HttpResponse("saved")

def updatef1(request):
    user = User.objects.get(pk=request.user.id)
    data = request.GET.get('f1', None)
    user.profile.f1_status = data
    user.save()
    return HttpResponse("saved")

