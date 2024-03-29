from django.http import HttpResponse
from django.shortcuts import render
from .form import EventRegisterForm, GuestFormSet
from django.contrib.auth.decorators import login_required
from index.views import active_events, droute


@login_required()
def events_register(request):
    base_template_name = 'member/base.html'
    event = active_events()
    dr = droute()
    user = request.user.id
    context = {'base_template_name': base_template_name, 'event': event, 'user': user, 'dr': dr}
    if request.method == 'POST':
        form = EventRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index/stripe_events.html', context)
        else:
            HttpResponse('Form did not go through, there was an error.')
    else:
        initial_data = {'member': user, 'active_events': event}
        form = EventRegisterForm(initial=initial_data)
        context = {'form': form, 'base_template_name': base_template_name, 'event': event, 'dr': dr, 'user': user}
        return render(request, 'event/events_register.html', context)


def guest_register(request):
    base_template_name = 'index/base.html'
    event = active_events()
    context = {'base_template_name': base_template_name, 'event': event}
    if request.method == 'POST':
        formset = GuestFormSet(data=request.POST)
        if formset.is_valid():
            formset.save()
            return render(request, 'index/stripe_events.html', context)
        else:
            HttpResponse('Form did not go through, there was an error.')
    else:
        formset = GuestFormSet()
        context = {'formset': formset, 'base_template_name': base_template_name, 'event': event}
        return render(request, 'event/guest_register.html', context)
