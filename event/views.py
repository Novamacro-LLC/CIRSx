from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import EventRegisterForm, GuestFormSet
from .models import EventRegistration
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError


@login_required()
def events_register(request):
    context = {}

    class BirdAddView(TemplateView):
        template_name = "add_bird.html"

        def get(self, *args, **kwargs):
            formset = BirdFormSet(queryset=Bird.objects.none())
            return self.render_to_response({'bird_formset': formset})

        # Define method to handle POST request
        def post(self, *args, **kwargs):
            formset = BirdFormSet(data=self.request.POST)

            # Check if submitted forms are valid
            if formset.is_valid():
                formset.save()
                return redirect(reverse_lazy("bird_list"))

            return self.render_to_response({'bird_formset': formset})

    return render(request, 'event/events_register.html', context)

