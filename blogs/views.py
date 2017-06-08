from django.shortcuts import render
from .models import Posts

def index(request):
    '''show some info''' 
    content = Posts.objects.order_by('date_added')
    context = {'content': content[:4]} #splice indicates that only four blog posts will be shown
    return render(request, 'blogs/index.html', context)
