from django.contrib.auth import views as auth_views
from .models import News
from rest_framework import serializers, viewsets, routers
from . import views
from django.conf.urls import include, url
from django.views.generic import ListView
from blog import views
from .models import Post




class DataSerilizer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ( 'source','title','description',
                   'date','time','author','image','link'
                  )
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date','published_date')
class DataViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = DataSerilizer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()[:1]
    serializer_class = PostSerializer



router = routers.DefaultRouter()
router.register(r'data', DataViewSet)



urlpatterns = [
    url(r'^update/$', views.update, name='update'),
    url(r'^updatedb/$', views.updatedb, name='updatedb'),

    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^$', views.index, name='index'),
    url(r'^feed/$', views.MultipleModelView.as_view(), name='news_list'),
    # url(r'^feedupdate/$', views.MultipleModelView.as_view(), name='news_list'),

    url(r'^feed/news/(?P<slug>[-\w]+)$', views.NewsDetailView.as_view(), name='news'),
    # url(r'^feed/movie/(?P<slug>[-\w]+)$', views.MovieDetailView.as_view(), name='movie'),
    url(r'^feed/deletechip$', views.deletechip, name='deletechip'),
    url(r'^feed/addchip$', views.addchip, name='addchip'),
    url(r'^feed/search/$', views.search, name='search'),
    url(r'^feed/clear/$', views.clear, name='clear'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^', include(router.urls)),
    url(r'^articles/comments/', include('django_comments.urls')),
    url(r'^comments/', include('django_comments.urls')),

]
