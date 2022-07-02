from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from account.forms import RegistrationForm


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
