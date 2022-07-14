from django.shortcuts import render, redirect


def events_register(request):
    return render(request, 'event/events_register.html',)

