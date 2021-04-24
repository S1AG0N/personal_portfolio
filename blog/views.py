from django.shortcuts import render
from .models import Blog


def home(request):
    sample = Blog.objects.all()
    return render(request, 'blog/home.html', {'sample':sample})


def latest(request):
    sampl = Blog.objects.all()
    return render(request, 'blog/latest_news.html', {'sampl': sampl})