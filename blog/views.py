from django.shortcuts import render
from .models import Post1
from django.utils import timezone


# Create your views here.

def post_list(request):
    posts = Post1.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
