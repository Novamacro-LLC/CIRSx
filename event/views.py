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
    user = request.user.id
    context = {'base_template_name': base_template_name, 'event': event, 'user':user}
    if request.method == 'POST':
        form = EventRegisterForm(data=request.POST)
        print(form.data.get('event'))
        formset = GuestFormSet(data=request.POST)
        if formset.is_valid() and form.is_valid():
            form.save()
            event_reg = EventRegistration.objects.filter(event=form.data.get('event'), member=form.data.get('member'), attendance=form.data.get('attendance')).last()
            print(event_reg.id)
            #add event_reg to guest and input into database
            formset.save()
            return render(request, 'index/stripe_events.html', context)
        else:
            HttpResponse('Form did not go through, there was an error.')
    else:
        form = EventRegisterForm()
        formset = GuestFormSet(queryset=Guest.objects.none())
        context = {'formset': formset, 'form': form, 'base_template_name': base_template_name, 'event': event}
        return render(request, 'event/events_register.html', context)
