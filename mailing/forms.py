from django.forms import ModelForm
from django import forms


from mailing.models import MailingRecipient, Message, Mailing


class StyleForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingRecipientForm(StyleForm, ModelForm):
    """Форма для добавления клиента для рассылки"""
    class Meta:
        model = MailingRecipient
        exclude = ['author',]


class MessageForm(StyleForm, ModelForm):
    """Форма для добавления сообщения"""
    class Meta:
        model = Message
        fields = "__all__"


class MailingForm(StyleForm, ModelForm):
    """Форма для добавления рассылки"""
    class Meta:
        model = Mailing
        fields = ['start_date', 'end_date', 'message', 'recipients']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
