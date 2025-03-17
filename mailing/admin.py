from django.contrib import admin
from mailing.models import MailingRecipient, Message, Mailing


@admin.register(MailingRecipient)
class MailingRecipientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'commentary')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'message')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'status', 'message')

