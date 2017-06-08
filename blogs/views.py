from django.shortcuts import render
from .models import Posts

def index(request):
    '''show some info''' #TODO edit so that only five posts appear on the front page
    content = Posts.objects.order_by('date_added')
    context = {'content': content}
    return render(request, 'blogs/index.html', context)
