from django.shortcuts import render, redirect
from .models import Document
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from index.views import active_events



@login_required()
def tier_welcome(request):
    event = active_events()
    context = {'event': event}
    return render(request, 'member/tier_welcome.html', context)


@login_required()
def tier_videos(request):
    event = active_events()
    context = {'event': event}
    return render(request, 'member/tier_videos.html', context)


@login_required()
def bibliographies(request):
    bib = Document.objects.filter(doctyp_num=1).order_by('title')
    event = active_events()
    context = {'event': event, 'bib': bib}
    return render(request, 'member/bibliographies.html', context)


@login_required()
def research_papers(request):
    rsh = Document.objects.filter(doctyp_num=2).order_by('title')
    event = active_events()
    context = {'event': event, 'rsh': rsh}
    return render(request, 'member/research_papers.html', context)


@login_required()
def archived_events(request):
    event = active_events()
    context = {'event': event}
    return render(request, 'member/archived_events.html', context)


@login_required()
def deeper_dive(request):
    event = active_events()
    context = {'event': event}
    return render(request, 'member/deeper_dive.html', context)


@login_required()
def hopkinton(request):
    event = active_events()
    context = {'event': event}
    return render(request, 'member/hopkinton.html', context)


@login_required()
def podcasts(request):
    event = active_events()
    context = {'event': event}
    return render(request, 'member/podcasts.html', context)

@login_required()
def doc_search(request):
    q = request.GET.get('q')


    if q:
        vector = SearchVector('title', 'author', 'keywords', 'doc_txt')
        query = SearchQuery(q)
        search_headline = SearchHeadline('doc_txt', query)

        # videos = Video.objects.filter(title__search=q)
        # videos = Video.objects.annotate(search=vector).filter(search=query)
        # videos = Video.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.001).order_by('-rank')
        doc = Document.objects.annotate(rank=SearchRank(vector, query)).annotate(headline=search_headline).filter(
            rank__gte=0.001).order_by('-rank')

        p = Paginator(doc, 10)
        page = request.GET.get('page')
        docs = p.get_page(page)


    else:
        docs = None
        q = None

    context = {'q': q, 'docs': docs}
    return render(request, 'member/search.html', context)
