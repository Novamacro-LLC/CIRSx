from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import news
from .form import ContactForm
import datetime


def home(request):
    end_date = datetime.datetime.now()
    st_date = datetime.datetime.now() - datetime.timedelta(days=90)
    front = news.objects.filter(date_added__range=[st_date, end_date]).order_by('-date_added')
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
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['brad.davison@novamacro.net'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('home')
    return render(request, 'home/contact_us.html', {'form': form})


def environmental_glossary(request):
    return render(request, 'home/environmental_glossary.html', {})


def shoey(request):
    return render(request, 'home/shoey.html', {})
