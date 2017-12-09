"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from django.apps import apps



class UserSerializer(serializers.HyperlinkedModelSerializer):
    # profile = ProfileSerializer()
    room_status = serializers.CharField(source='profile.room_status')
    wheater_city = serializers.CharField(source='profile.wheater_city')
    wheater_satus = serializers.CharField(source='profile.wheater_satus')
    daily_status = serializers.CharField(source='profile.daily_status')
    verge_status = serializers.CharField(source='profile.verge_status')
    stock_status = serializers.CharField(source='profile.stock_status')
    movie_status = serializers.CharField(source='profile.movie_status')
    f1_status = serializers.CharField(source='profile.f1_status')


    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name','last_name','last_login','date_joined'
                  ,'room_status','wheater_city','wheater_satus','daily_status',
                  'verge_status','stock_status','movie_status','f1_status')



class DataView(viewsets.ModelViewSet):
    queryset = apps.get_app_config('fireworder').get_models()

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    url(r'^', include('fireworder.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += staticfiles_urlpatterns()
