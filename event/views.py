from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import EventRegisterForm, GuestFormSet
from .models import EventRegistration, Guest
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError
from index.views import active_events

@login_required()
def events_register(request):
    base_template_name = 'member/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    if request.method == 'POST':
        form = EventRegisterForm(data=request.POST)
        formset = GuestFormSet(data=request.POST)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            redirect('stripe_events', context)
        else:
            HttpResponse('Form did not go through, there was an error.')
    else:
        form = EventRegisterForm()
        formset = GuestFormSet(queryset=Guest.objects.none())
        context = {'formset': formset, 'form': form, 'base_template_name': base_template_name, 'event': event}
        return render(request, 'event/events_register.html', context)
