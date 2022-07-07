from django.contrib import admin
from .models import Account, Country
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (('Permissions', {'fields': ('groups',)}),)


admin.site.register(Account, AccountAdmin)
admin.site.register(Country)
