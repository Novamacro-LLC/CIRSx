from django.shortcuts import render


def tier_welcome(request):
    return render(request, 'member/tier_welcome.html', {})


def tier_videos(request):
    return render(request, 'member/tier_videos.html', {})
