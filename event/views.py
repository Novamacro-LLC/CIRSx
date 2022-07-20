from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import EventRegisterForm


def events_register(request):
    if request.method == 'GET':
        form = EventRegisterForm()
        context = {'form': form}
        return render(request, 'event/events_register.html', context)
    else:
        form = EventRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
        else:
            return HttpResponse('Form is invalid')




