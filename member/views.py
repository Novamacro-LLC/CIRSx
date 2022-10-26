from django.shortcuts import render, redirect
from .models import Document, DocumentRoute
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from index.views import active_events, droute
from event.models import Event


@login_required()
def tier_welcome(request):
    event = active_events()
    dr = droute()
    context = {'event': event, 'dr': dr}
    return render(request, 'member/tier_welcome.html', context)


@login_required()
def tier_videos(request):
    event = active_events()
    dr = droute()
    context = {'event': event, 'dr': dr}
    return render(request, 'member/tier_videos.html', context)


@login_required()
def bibliographies(request):
    bib = Document.objects.filter(doctyp_num=1).order_by('title')
    event = active_events()
    dr = droute
    context = {'event': event, 'bib': bib, 'dr': dr}
    return render(request, 'member/bibliographies.html', context)


@login_required()
def research_papers(request):
    rsh = Document.objects.filter(doctyp_num=2).order_by('title')
    event = active_events()
    dr = droute
    context = {'event': event, 'rsh': rsh, 'dr': dr}
    return render(request, 'member/research_papers.html', context)


@login_required()
def past_events(request):
    event = active_events()
    dr = droute
    past_events = Event.objects.filter(active=False)
    event_details = past_events.last()
    context = {'event': event, 'dr': dr, 'past_events': past_events, 'event_details': event_details}
    return render(request, 'member/archived_events.html', context)


@login_required()
def archived_events(request, name=None):
    event = active_events()
    dr = droute
    past_events = Event.objects.filter(active=False)
    if name:
        event_details = Event.objects.filter(event_name=name).first()
        docs = Document.objects.filter(event=event_details.id)
        sponsor = event_details.sponsors.all()
        speaker = event_details.speakers.all()
        context = {'event': event, 'dr': dr, 'past_events': past_events, 'event_details': event_details, 'docs': docs,
                   'sponsor': sponsor, 'speaker': speaker}
        return render(request, 'member/archived_events.html', context)
    else:
        context = {'event': event, 'dr': dr, 'past_events': past_events}
        return render(request, 'member/archived_events.html', context)


@login_required()
def doc_search(request):
    event = active_events()
    dr = droute()
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

    context = {'q': q, 'docs': docs, 'event': event, 'dr': dr}
    return render(request, 'member/search.html', context)


@login_required()
def doc_route(request, name):
    base_template_name = 'member/base.html'
    event = active_events()
    dr = droute()
    dr_info = DocumentRoute.objects.get(document_route=name)
    content = Document.objects.filter(doc_route_id=dr_info.id, doctyp_num_id=3)
    context = {'base_template_name': base_template_name, 'event': event, 'dr_info': dr_info, 'dr': dr,
               'content': content}
    return render(request, 'member/doc_route.html', context)
