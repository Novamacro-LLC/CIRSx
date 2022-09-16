from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import News
from event.models import Event
from .form import ContactForm

import datetime


def active_events():
    event_name = Event.objects.filter(active=True)
    return event_name


def home(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    end_date = datetime.datetime.now()
    st_date = datetime.datetime.now() - datetime.timedelta(days=90)
    front = News.objects.filter(date_added__range=[st_date, end_date]).order_by('-date_added')
    context = {'front': front, 'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/home.html', context)


def subscribe(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/subscribe.html', context)


def about_us(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/about_us.html', context)


def conference(request, name):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    event_info = Event.objects.filter(event_name=name)
    context = {'base_template_name': base_template_name, 'event': event, 'event_info': event_info}
    return render(request, 'index/conference.html', context)


def sponsor(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/sponsor.html', context)


def medical_glossary(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/medical_glossary.html', context)


def speakers(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/speakers.html', context)


def contact_us(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = 'support@novamacro.net'
            subject = 'New website message'
            message = 'You have received a new message from the website.  Please login to the admin site to check'
            try:
                send_mail(subject, message, email, ['brad.davison@novamacro.net'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Message has been sent')

    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event, 'form': form}
    return render(request, 'index/contact_us.html', context)


def environmental_glossary(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/environmental_glossary.html', context)


def shoey(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/shoey.html', context)


def stripe_pro(request):
    event = active_events()
    context = {'event': event}
    return render(request, 'index/stripe_pro.html', context)


def stripe_patient(request):
    event = active_events()
    context = {'event': event}
    return render(request, 'index/stripe_patient.html', context)


def stripe_events(request):
    event = active_events()
    context = {'event': event}
    return render(request, 'index/stripe_events.html', context)


def placeholder(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/placeholder.html', context)


