from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import EventRegisterForm, MarksForm
from .models import EventRegistration, Marks
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required


@login_required()
def events_register(request):
    context = {}
    MarksForm = modelformset_factory(Marks, form=MarksForm)
    if request.method == 'GET':
        form = EventRegisterForm()
        context = {'form': form}
        return render(request, 'event/events_register.html', context)
    else:
        form = EventRegisterForm(request.POST)
        if form.is_valid():
            form.event = True
            form.save()
            redirect('index')
        else:
            return HttpResponse('Form is invalid')

        context['formset'] = formset
        context['form'] = form
        return render(request, 'index', context)

