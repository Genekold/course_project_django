from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms


from mailing.models import MailingRecipient, Message, Mailing


class StyleForm:
    """Класс для наследования стилизации форм"""
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
        fields = ['end_date', 'message']
        widgets = {
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


class MailingFormUpdate(StyleForm, ModelForm):
    """Форма для изменения рассылки рассылки"""

    class Meta:
        model = Mailing
        fields = ['end_date', 'message', 'recipients']
        widgets = {
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        mailing = kwargs.get('instance', None)
        author = mailing.author
        super().__init__(*args, **kwargs)

        if mailing:
            self.fields['recipients'].queryset = MailingRecipient.objects.filter(author=author)


class MailingAddRecipientForm(StyleForm, ModelForm):
    """Форма для добавления в рссылку получателей"""
    class Meta:
        model = Mailing
        fields = ['recipients',]

    def __init__(self, *args, **kwargs):
        mailing = kwargs.get('instance', None)
        author = mailing.author
        super().__init__(*args, **kwargs)

        if mailing:
            self.fields['recipients'].queryset = MailingRecipient.objects.filter(author=author)
