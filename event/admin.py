from django.contrib import admin
from .models import Event, EventOffer, EventRegistration, Sponsor, Speaker, Expertise


admin.site.register(EventOffer)
admin.site.register(Sponsor)
admin.site.register(Speaker)
admin.site.register(Expertise)
admin.site.register(EventRegistration)


class SpeakerInline(admin.TabularInline):
    model = Event.speakers.through


class SponsorInline(admin.TabularInline):
    model = Event.sponsors.through


@admin.register(Event)
class SpeakerAdmin(admin.ModelAdmin):
    inlines = (SpeakerInline, SponsorInline,)
    exclude = ('speakers', 'sponsors',)
