from django.shortcuts import render
from .models import Posts
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def index(request):
    '''show some info'''
    articles = Posts.objects.order_by('-date_added')
    context = {'articles': articles[:4]} #splice indicates that only four blog posts will be shown.  Very important.
    return render(request, 'blogs/index.html', context)

def archives(request):
    archives = Posts.objects.order_by('-date_added')
    context = {'archives': archives}
    return render(request, 'blogs/archives.html', context)

def article(request, article_id):
    article = Posts.objects.get(id=article_id)
    content = Posts.objects.order_by('-date_added')
    context = {'article': article, 'content': content}
    return render(request, 'blogs/article.html', context)


#TODO maybe shorten the posts on the front page so they don't take up the entire page
# by adding an ellipsis at the end.  Then have a link on the title so you can go read
# the full article.  Also need an archive page that contains everything no matter what.
