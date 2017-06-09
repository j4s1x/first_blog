from django.shortcuts import render
from .models import Posts

def index(request):
    '''show some info'''
    content = Posts.objects.order_by('date_added')
    context = {'content': content[:4]} #splice indicates that only four blog posts will be shown
    return render(request, 'blogs/index.html', context)

def article(request, article_id):
    article = Posts.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'blogs/article.html', context)


#TODO maybe shorten the posts on the front page so they don't take up the entire page
# by adding an ellipsis at the end.  Then have a link on the title so you can go read
# the full article.  Also need an archive page that contains everything no matter what.
