from django.contrib.auth import views as auth_views
from .models import News
from rest_framework import serializers, viewsets, routers
from . import views
from django.conf.urls import include, url
from django.views.generic import ListView



class DataSerilizer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ( 'source','title','description',
                   'date','time','author','image','link'
                  )

class DataViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = DataSerilizer



router = routers.DefaultRouter()
router.register(r'data', DataViewSet)



urlpatterns = [
    url(r'^update/$', views.update, name='update'),
    url(r'^$', views.index, name='index'),
    url(r'^feed/$', views.MultipleModelView.as_view(), name='news_list'),
    url(r'^feed/news/(?P<slug>[-\w]+)$', views.NewsDetailView.as_view(), name='news'),
    url(r'^feed/movie/(?P<slug>[-\w]+)$', views.MovieDetailView.as_view(), name='movie'),
    url(r'^deletechip/$', views.deletechip, name='deletechip'),
    url(r'^addchip/$', views.addchip, name='addchip'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^', include(router.urls)),

]

