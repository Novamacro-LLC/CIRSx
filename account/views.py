from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from account.form import RegistrationForm, AccountAuthenticationForm


def register(request, tier):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            pro = Group.objects.get(name=tier)
            user.groups.add(pro)
            return redirect('tier_welcome')
    else:
        form = RegistrationForm()
        context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def login_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect('tier_welcome')
    if request == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.email
            password = form.password
            authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('tier_welcome')
    else:
        form = AccountAuthenticationForm()

    context = {'form': form}
    return render(request, 'registration/login.html', context)
