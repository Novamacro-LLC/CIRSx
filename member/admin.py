from django.contrib import admin
from .models import Audience, DocumentType, Document, Event, Expertise, Sponsor, EventOffer, Speaker

admin.site.register(Audience)
admin.site.register(DocumentType)
admin.site.register(Document)
#admin.site.register(Event)
admin.site.register(EventOffer)
admin.site.register(Expertise)
admin.site.register(Sponsor)
admin.site.register(Speaker)


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('doctyp_name',)


class SpeakerInline(admin.TabularInline):
    model = Event.speakers.through


class SponsorInline(admin.TabularInline):
    model = Event.sponsors.through


@admin.register(Event)
class SpeakerAdmin(admin.ModelAdmin):
    inlines = (SpeakerInline, SponsorInline,)
    exclude = ('speakers', 'sponsors',)


