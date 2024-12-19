from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MailingRecipientForm
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
    """Класс изменения получателя"""
    model = MailingRecipient
    success_url = reverse_lazy("mailing:recipient_list")
