from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html', {})


def subscribe(request):
    return render(request, 'home/subscribe.html', {})


def about_us(request):
    return render(request, 'home/about_us.html', {})


def conference(request):
    return render(request, 'home/conference.html', {})


def sponsor(request):
    return render(request, 'home/sponsor.html', {})


def medical_glossary(request):
    return render(request, 'home/medical_glossary.html', {})


def speakers(request):
    return render(request, 'home/speakers.html', {})


def contact_us(request):
    return render(request, 'home/contact_us.html', {})
