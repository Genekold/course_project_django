from django import template

from mailing.models import MailingRecipient

register = template.Library()


@register.simple_tag
def get_mailing(pk):
    recipient = MailingRecipient.objects.filter(pk=pk)
    return len(recipient[0].recipients.all())
