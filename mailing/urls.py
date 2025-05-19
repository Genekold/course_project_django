from django.urls import path
from mailing.views import MailingRecipientListView, MailingRecipientDetailView, MailingRecipientCreateView, \
    MailingRecipientUpdateView, MailingRecipientDeleteView, MessageListView, MessageDetailView, MessageCreateView, \
    MessageUpdateView, MessageDeleteView, MailingListView, MailingDetailView, MailingCreateView, MailingDeleteView, \
    MailingUpdateView, index, statistic_mailing, send_mail, UserListView, user_blocking, user_unblocking, \
    mailing_blocking, mailing_unblocking, MailingAddRecipient
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    path("", index, name='index'),

    path("recipient_list/", MailingRecipientListView.as_view(), name='recipient_list'),
    path("recipient/<int:pk>/", MailingRecipientDetailView.as_view(), name='recipient_detail'),
    path("recipient/create/", MailingRecipientCreateView.as_view(), name='recipient_create'),
    path("recipient/<int:pk>/update/", MailingRecipientUpdateView.as_view(), name='recipient_update'),
    path("recipient/<int:pk>/delete/", MailingRecipientDeleteView.as_view(), name='recipient_delete'),

    path("message_list/", MessageListView.as_view(), name="message_list"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("message/create/", MessageCreateView.as_view(), name="message_create"),
    path("message/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),

    path("mailing_list/", MailingListView.as_view(), name="mailing_list"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing/create/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing/<int:pk>/update/", MailingUpdateView.as_view(), name="mailing_update"),
    path("mailing/<int:pk>/add_recipient/", MailingAddRecipient.as_view(), name="add_recipient"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"),
    path("mailing/statistic/<int:mailing_id>/", statistic_mailing, name="mailing_statistic"),
    path("mailing/send_ok/<int:mailing_id>/", send_mail, name="send_ok"),

    path("user_list/", UserListView.as_view(), name="user_list"),

    path("user_list/block/<int:user_id>/", user_blocking, name="user_blocking"),
    path("user_list/unblock/<int:user_id>/", user_unblocking, name="user_unblocking"),

    path("mailing_list/block/<int:mailing_id>/", mailing_blocking, name="mailing_blocking"),
    path("mailing_list/unblock/<int:mailing_id>/", mailing_unblocking, name="mailing_unblocking"),
]
