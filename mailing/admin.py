from django.contrib import admin
from mailing.models import MailingRecipient, Message


@admin.register(MailingRecipient)
class MailingRecipientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'commentary')
