import datetime

from django.shortcuts import render
from .models import news


def home(request):
    end_date = datetime.datetime.now()
    st_date = datetime.datetime.now() - datetime.timedelta(days=90)
    front = news.objects.filter(date_added__range=[st_date, end_date])
    context = {'front': front}
    return render(request, 'home/home.html', context)


def subscribe(request):
    return render(request, 'home/subscribe.html', {})


def about_us(request):
    return render(request, 'home/about_us.html', {})


def conference(request):
    return render(request, 'home/conference1.html', {})


def sponsor(request):
    return render(request, 'home/sponsor.html', {})


def medical_glossary(request):
    return render(request, 'home/medical_glossary.html', {})


def speakers(request):
    return render(request, 'home/speakers.html', {})


def contact_us(request):
    return render(request, 'home/contact_us.html', {})


