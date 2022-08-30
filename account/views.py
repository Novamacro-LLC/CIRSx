from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django.http import HttpResponse
from account.form import RegistrationForm, AccountAuthenticationForm
from index.views import active_events


def register(request, tier):

    form = RegistrationForm()
    context = {'form': form, 'tier': tier}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            pro = Group.objects.get(name=tier)
            user.groups.add(pro)
            return render(request, 'member/tier_welcome.html', {})
        else:
            return HttpResponse('Data is not clean', form.errors)
    else:
        event = active_events()
        context = {'event': event}
        return render(request, 'registration/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def login_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect('tier_welcome')
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
            return redirect('tier_welcome')
    else:
        form = AccountAuthenticationForm()
    event = active_events()
    context = {'form': form, 'event': event}
    return render(request, 'registration/login.html', context)
