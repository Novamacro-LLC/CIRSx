from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import News
from .form import ContactForm

import datetime


def home(request):
    end_date = datetime.datetime.now()
    st_date = datetime.datetime.now() - datetime.timedelta(days=90)
    front = News.objects.filter(date_added__range=[st_date, end_date]).order_by('-date_added')
    context = {'front': front}
    return render(request, 'home/home.html', context)


def subscribe(request):
    return render(request, 'home/subscribe.html', {})


def about_us(request):
    return render(request, 'home/about_us.html', {})


def conference(request):
    return render(request, 'home/conference.html', {})


def sponsor(request):
    return render(request, 'home/sponsor.html', {})


def medical_glossary(request):
    return render(request, 'home/medical_glossary.html', {})


def speakers(request):
    return render(request, 'home/speakers.html', {})


def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = 'support@novamacro.net'
            subject = 'New website message'
            message = 'You have received a new message from 1the website.  Please login to the admin site to check'
            try:
                send_mail(subject, message, email, ['brad.davison@novamacro.net'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Message has been sent')
    return render(request, 'home/contact_us.html', {'form': form})


def environmental_glossary(request):
    return render(request, 'home/environmental_glossary.html', {})


def shoey(request):
    return render(request, 'home/shoey.html', {})


def stripe_pro(request):
    return render(request, 'home/stripe_pro.html', {})


def stripe_patient(request):
    return render(request, 'home/stripe_patient.html', {})


def test(request):
    return render(request, 'home/test.html'),


