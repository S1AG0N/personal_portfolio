from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def about(request):
    pro = Project.objects.all()
    return render(request, 'portfolio/about.html', {'pro': pro})