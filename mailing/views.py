from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MailingRecipientForm, MessageForm
from mailing.models import MailingRecipient, Message


class MailingRecipientListView(ListView):
    """Класс представления списка получателей"""
    model = MailingRecipient


class MailingRecipientDetailView(DetailView):
    """Класс детального представления одного получателя"""
    model = MailingRecipient


class MailingRecipientCreateView(CreateView):
    """Класс создания получателя"""
    model = MailingRecipient
    form_class = MailingRecipientForm
    success_url = reverse_lazy("mailing:recipient_list")


class MailingRecipientUpdateView(UpdateView):
    """Класс изменения получателя"""
    model = MailingRecipient
    form_class = MailingRecipientForm
    success_url = reverse_lazy("mailing:recipient_list")


class MailingRecipientDeleteView(DeleteView):
    """Класс удаления получателя"""
    model = MailingRecipient
    success_url = reverse_lazy("mailing:recipient_list")


class MessageListView(ListView):
    """Класс представления сообщения"""
    model = Message


class MessageDetailView(DetailView):
    """Класс детального сообщения"""
    model = Message


class MessageCreateView(CreateView):
    """Класс создания сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


class MessageUpdateView(UpdateView):
    """Класс изменения сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


class MessageDeleteView(DeleteView):
    """Класс удаления сообщения"""
    model = Message
    success_url = reverse_lazy("mailing:message_list")
