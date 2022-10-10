from django.contrib import admin
from .models import Audience, DocumentType, Document, DocumentRoute

admin.site.register(Audience)
admin.site.register(DocumentType)
admin.site.register(Document)
admin.site.register(DocumentRoute)


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('doctyp_name',)



