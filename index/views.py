from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import News
from event.models import Event
from .form import ContactForm
from index.views import active_events

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


def conference(request, event_id):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
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
            message = 'You have received a new message from 1the website.  Please login to the admin site to check'
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
    return render(request, 'index/stripe_pro.html', )


def stripe_patient(request):
    return render(request, 'index/stripe_patient.html', )


def stripe_events(request):
    return render(request, 'index/stripe_events.html', )


def test(request):
    return render(request, 'index/test.html'),


def placeholder(request):
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    return render(request, 'index/placeholder.html', context)


