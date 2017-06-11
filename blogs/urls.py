'''defines the url patterns for [blogs]'''

from django.conf.urls import url
from . import views

urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'), # ^$ beginning to end of string
    #article page
    url(r'^articles/$', views.articles, name = 'articles'),
    #specific article
    url(r'^articles/(?P<article_id>\d+)/$',views.article, name='article')
    # comment out for bugs url(r'^articles/article/(?P<article_id>\d+)/$', views.article, name = 'article'),
    ]
