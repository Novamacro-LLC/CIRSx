from django.shortcuts import render, redirect
from .models import Document
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from index.views import active_events


@login_required()
def tier_welcome(request):
    event = active_events()
    context = {'event': event, 'event_info': event_info}
    return render(request, 'member/tier_welcome.html', context)


@login_required()
def tier_videos(request):
    event = active_events()
    context = {'event': event, 'event_info': event_info}
    return render(request, 'member/tier_videos.html', context)


@login_required()
def bibliographies(request):
    bib = Document.objects.filter(doctyp_num=1).order_by('title')
    event = active_events()
    context = {'event': event, 'bib': bib, 'event_info': event_info}
    return render(request, 'member/bibliographies.html', context)


@login_required()
def research_papers(request):
    rsh = Document.objects.filter(doctyp_num=2).order_by('title')
    event = active_events()
    context = {'event': event, 'rsh': rsh, 'event_info': event_info}
    return render(request, 'member/research_papers.html', context)


@login_required()
def archived_events(request):
    event = active_events()
    context = {'event': event, 'event_info': event_info}
    return render(request, 'member/archived_events.html', context)


@login_required()
def deeper_dive(request):
    event = active_events()
    context = {'event': event, 'event_info': event_info}
    return render(request, 'member/deeper_dive.html', context)


@login_required()
def hopkinton(request):
    event = active_events()
    context = {'event': event, 'event_info': event_info}
    return render(request, 'member/hopkinton.html', context)


@login_required()
def podcasts(request):
    event = active_events()
    context = {'event': event, 'event_info': event_info}
    return render(request, 'member/podcasts.html', context)