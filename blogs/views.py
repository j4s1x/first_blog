from django.shortcuts import render
from .models import Posts
from .forms import CommentForm
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
    comments = article.comments_set.order_by('-date_added')
    if request.method != 'POST':
        #no data submitted; create blank form
        form = CommentForm()
    else:
        #POST data submitted, process data
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.comments = comments
            new_comment.save()
            return HttpResponseRedirect(reverse('blogs:article', args=[article_id]))

    context = {'article': article, 'comments': comments, 'form': form}
    return render(request, 'blogs/article.html', context)
