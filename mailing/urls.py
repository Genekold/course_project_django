from django.urls import path
from mailing.views import MailingRecipientListView, MailingRecipientDetailView, MailingRecipientCreateView, \
    MailingRecipientUpdateView, MailingRecipientDeleteView
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    path("recipient_list/", MailingRecipientListView.as_view(), name='recipient_list'),
    path("recipient/<int:pk>", MailingRecipientDetailView.as_view(), name='recipient_detail'),
    path("recipient/create/", MailingRecipientCreateView.as_view(), name='recipient_create'),
    path("recipient/<int:pk>/update/", MailingRecipientUpdateView.as_view(), name='recipient_update'),
    path("recipient/<int:pk>/delete/", MailingRecipientDeleteView.as_view(), name='recipient_delete')
]
