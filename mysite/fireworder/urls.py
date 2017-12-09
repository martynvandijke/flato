from django.contrib.auth import views as auth_views
from .models import Data
from rest_framework import serializers, viewsets, routers
from . import views
from django.conf.urls import include, url


class DataSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('f1_round','f1_season','f1_wiki','f1_name','f1_date','f1_time',
                  'movie_poster','movie_vote','movie_title', 'movie_overview',
                  'verge_author','verge_title','verge_description','verge_url','verge_image',
                  'wheater_cirtykey','wheater_country','wheater_province',
                  'wheater_day1_min', 'wheater_day1_max', 'wheater_day1_icon',
                  "wheater_day2_min",'wheater_day2_max', 'wheater_day2_icon',
                  "wheater_day3_min",'wheater_day3_max', 'wheater_day3_icon',
                  'daily_imageurl','daily_imagelink',
                  'stock_companyname','stock_exchange','stock_price','stock_changepercent'


                  )

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()[:1]
    serializer_class = DataSerilizer



router = routers.DefaultRouter()
router.register(r'data', DataViewSet)



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^force/$', views.force, name='force'),
    url(r'^update$', views.update, name='update'),
    url(r'^wheater$', views.wheater, name='wheater'),
    url(r'^updatestock$', views.updatestock, name='updatestock'),
    url(r'^updatemovie$', views.updatemovie, name='updatemovie'),
    url(r'^updatedaily$', views.updatedaily, name='updatedaily'),
    url(r'^updateroom$', views.updateroom, name='updateroom'),
    url(r'^updatewheater$', views.updatewheater, name='updatewhetaer'),
    url(r'^updateverge$', views.updateverge, name='updateverge'),
    url(r'^updatef1$', views.updatef1, name='updatef1'),
    url(r'^updatedb/$', views.updatedb, name='updatedb'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^', include(router.urls)),
]
