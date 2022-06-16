from django.contrib import admin
from .models import Audience, DocumentType, Document

admin.site.register(Audience)
admin.site.register(DocumentType)
admin.site.register(Document)


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('doctyp_name',)
