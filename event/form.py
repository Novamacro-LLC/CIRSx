from django import forms
from .models import EventRegistration, Guest
from django.forms import modelformset_factory


class EventRegisterForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['event',
                  'member',
                  'attendance']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


GuestFormSet = modelformset_factory(
    Guest, fields=(
        "guest_name",
        "guest_email",
        "attendance"), extra=0
)


#class MemberForm(forms.ModelForm):
#    class Meta:
#        model = Registration
#        fields = (
#            "member",
#            "event"
#        )

#MemberFormSet = inlineformset_factory(
#   Member,
#   Event,
#   MemberForm,
#   can_delete=False
#)
