from django.shortcuts import render
from .models import Posts
from .models import Comments
from .forms import CommentForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def index(request):
    '''show some info'''
    articles = Posts.objects.order_by('-date_added')
    context = {'articles': articles[:3]} #splice indicates that only 3 blog posts will be shown.
    return render(request, 'blogs/index.html', context)

def archives(request):
    archives = Posts.objects.order_by('-date_added')
    context = {'archives': archives}
    return render(request, 'blogs/archives.html', context)

def article(request, article_id):
    article = Posts.objects.get(id=article_id)
    post = Posts.objects.get(id=article_id) #important...calls the ForeignKey for database
    comm = post.comments_set.order_by('-date_added')
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.post = post
            new_entry.save()
            return HttpResponseRedirect(reverse('blogs:article', args=[article_id]))
    context = {'article': article,'form':form, 'comm': comm}
    return render(request, 'blogs/article.html', context)

def about(request):
    return render(request, 'blogs/aboutauthor.html')

# css style information below
'''
<link rel="stylesheet" href="{% static '/css/bootstrap.min.css' %}">
<link rel="stylesheet" href="{% static '/css/bootstrap-theme.min.css' %}">
<link rel="stylesheet" href="{% static '/css/blog.css' %}">
'''
