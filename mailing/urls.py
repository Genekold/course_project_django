from django.urls import path
from mailing.views import MailingRecipientListView, MailingRecipientDetailView, MailingRecipientCreateView, \
    MailingRecipientUpdateView, MailingRecipientDeleteView, MessageListView, MessageDetailView, MessageCreateView, \
    MessageUpdateView, MessageDeleteView, MailingListView, MailingDetailView, MailingCreateView, MailingDeleteView, \
    MailingUpdateView, home
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    path("", home, name='home'),

    path("recipient_list/", MailingRecipientListView.as_view(), name='recipient_list'),
    path("recipient/<int:pk>", MailingRecipientDetailView.as_view(), name='recipient_detail'),
    path("recipient/create/", MailingRecipientCreateView.as_view(), name='recipient_create'),
    path("recipient/<int:pk>/update/", MailingRecipientUpdateView.as_view(), name='recipient_update'),
    path("recipient/<int:pk>/delete/", MailingRecipientDeleteView.as_view(), name='recipient_delete'),

    path("message_list/", MessageListView.as_view(), name="message_list"),
    path("message/<int:pk>", MessageDetailView.as_view(), name="message_detail"),
    path("message/create", MessageCreateView.as_view(), name="message_create"),
    path("message/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),

    path("mailing_list/", MailingListView.as_view(), name="mailing_list"),
    path("mailing/<int:pk>", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing/create", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing/<int:pk>/update/", MailingUpdateView.as_view(), name="mailing_update"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"),
]
