from django.forms import ModelForm

from mailing.models import MailingRecipient


class StyleFormBlog:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingRecipientForm(StyleFormBlog, ModelForm):
    class Meta:
        model = MailingRecipient
        fields = "__all__"