'''defines the url patterns for [blogs]'''

from django.conf.urls import url
from . import views

urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'), # ^$ beginning to end of string
    url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'), #link to specific article page
]
