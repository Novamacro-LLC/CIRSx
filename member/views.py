from django.shortcuts import render, redirect
from .models import Document
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required()
def tier_welcome(request):
    return render(request, 'member/tier_welcome.html', {})


@login_required()
def tier_videos(request):
    return render(request, 'member/tier_videos.html', {})


@login_required()
def bibliographies(request):
    bib = Document.objects.filter(doctyp_num=1).order_by('title')
    context = {'bib': bib}
    return render(request, 'member/bibliographies.html', context)


@login_required()
def research_papers(request):
    rsh = Document.objects.filter(doctyp_num=2).order_by('title')
    context = {'rsh': rsh}
    return render(request, 'member/research_papers.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')
