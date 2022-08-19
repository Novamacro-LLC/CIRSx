from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import EventRegisterForm, MarksForm
from .models import EventRegistration, Marks
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError


@login_required()
def events_register(request):
    context = {}
    MarksFormset = modelformset_factory(Marks, form=MarksForm)
    form = EventRegisterForm(request.POST or None)
    formset = MarksFormset(request.POST or None, queryset=Marks.objects.none(), prefix='marks')
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    events_register = form.save(commit=False)
                    events_register.save()

                    for mark in formset:
                        data = mark.save(commit=False)
                        data.events = events_register
                        data.save()
            except IntegrityError:
                print("Error Encountered")

            return redirect('multi_forms:list')

    context['formset'] = formset
    context['form'] = form
    if request.user.is_authenticated:
        base_template_name = 'member/base.html'
    else:
        base_template_name = 'index/base.html'
    context = {base_template_name: 'base_template_name'}
    return render(request, 'event/events_register.html', context)

