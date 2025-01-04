from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MailingRecipientForm, MessageForm, MailingForm
from mailing.models import MailingRecipient, Message, Mailing


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

    def get_success_url(self):
        return reverse("mailing:recipient_detail", args=[self.kwargs.get('pk')])


class MailingRecipientDeleteView(DeleteView):
    """Класс удаления получателя"""
    model = MailingRecipient
    success_url = reverse_lazy("mailing:recipient_list")


class MessageListView(ListView):
    """Класс представления сообщения"""
    model = Message


class MessageDetailView(DetailView):
    """Класс детального представления сообщения"""
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

    def get_success_url(self):
        return reverse("mailing:message_detail", args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    """Класс удаления сообщения"""
    model = Message
    success_url = reverse_lazy("mailing:message_list")


class MailingListView(ListView):
    """Класс представления рассылки"""
    model = Mailing


class MailingDetailView(DetailView):
    """Класс детального представления рассылки"""
    model = Mailing

    def get_context_data(self, **kwargs):
        recipients = MailingRecipient.objects.all()
        context = super().get_context_data(**kwargs)
        for recipient in recipients:
            print(recipient)

        context['recipients'] = recipients
        return context


class MailingCreateView(CreateView):
    """Класс создания рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")


class MailingUpdateView(UpdateView):
    """Класс изменения рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")

    def get_success_url(self):
        return reverse("mailing:mailing_detail", args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    """Класс удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")


def home(request):
    return render(request, 'mailing/base.html')
