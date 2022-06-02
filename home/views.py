from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home/home.html', {})


def subscribe(request):
    return render(request, 'home/subscribe.html', {})


def about_us(request):
    return render(request, 'home/about_us.html', {})


def conference(request):
    return render(request, 'home/conference.html', {})
