from django.shortcuts import render, redirect
from .form import EventRegisterForm


def events_register(request):
    if request.method == 'GET':
        form = EventRegisterForm()
    return render(request, 'event/events_register.html',)



