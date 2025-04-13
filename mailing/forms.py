from django.forms import ModelForm
from django import forms


from mailing.models import MailingRecipient, Message, Mailing


class StyleForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingRecipientForm(StyleForm, ModelForm):
    class Meta:
        model = MailingRecipient
        fields = "__all__"


class MessageForm(StyleForm, ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class MailingForm(StyleForm, ModelForm):
    class Meta:
        model = Mailing
        fields = ['start_date', 'end_date', 'message', 'recipients']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
