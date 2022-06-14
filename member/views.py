from django.shortcuts import render


def tier_welcome(request):
    return render(request, 'member/tier_welcome.html', {})


def tier_videos(request):
    return render(request, 'member/tier_videos.html', {})


def bibliographies(request):
    return render(request, 'member/bibliographies.html', {})


def research_papers(request):
    return render(request, 'member/research_papers.html', {})
