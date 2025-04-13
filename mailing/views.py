from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MailingRecipientForm, MessageForm, MailingForm
from mailing.models import MailingRecipient, Message, Mailing, MailingAttempt
from mailing.services import MailingService
from users.models import User


class MailingRecipientListView(LoginRequiredMixin, ListView):
    """Класс представления списка получателей"""
    model = MailingRecipient

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.groups.filter(name="manager").exists():
            return qs
        return qs.filter(author=self.request.user)


class MailingRecipientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс детального представления одного получателя"""
    model = MailingRecipient
    permission_required = 'mailing.view_mailingrecipient'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return HttpResponseForbidden('У вас нет прав для просмотра этой страницы')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        recipient = MailingRecipient.objects.filter(pk=self.object.pk)
        mailings = recipient[0].recipients.all()
        context['mailings'] = mailings
        return context


class MailingRecipientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс создания получателя"""
    model = MailingRecipient
    form_class = MailingRecipientForm
    success_url = reverse_lazy("mailing:recipient_list")
    permission_required = 'mailing.add_mailingrecipient'

    def form_valid(self, form):
        recipient = form.save(commit=False)
        recipient.author = self.request.user
        return super().form_valid(form)


class MailingRecipientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Класс изменения получателя"""
    model = MailingRecipient
    form_class = MailingRecipientForm
    success_url = reverse_lazy("mailing:recipient_list")
    permission_required = 'mailing.change_mailingrecipient'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return HttpResponseForbidden('У вас нет прав для просмотра этой страницы')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse("mailing:recipient_detail", args=[self.kwargs.get('pk')])


class MailingRecipientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Класс удаления получателя"""
    model = MailingRecipient
    success_url = reverse_lazy("mailing:recipient_list")
    permission_required = 'mailing.delete_mailingrecipient'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return HttpResponseForbidden('У вас нет прав для просмотра этой страницы')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class MessageListView(ListView):
    """Класс представления сообщения"""
    model = Message


class MessageDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс детального представления сообщения"""
    model = Message
    permission_required = 'mailing.view_message'


class MessageCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс создания сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")
    permission_required = 'mailing.add_message'

    def form_valid(self, form):
        mailing = form.save(commit=False)
        mailing.author = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Класс изменения сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")
    permission_required = 'mailing.change_message'

    def get_success_url(self):
        return reverse("mailing:message_detail", args=[self.kwargs.get('pk')])


class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Класс удаления сообщения"""
    model = Message
    success_url = reverse_lazy("mailing:message_list")
    permission_required = 'mailing.delete_message'


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Класс представления рассылки"""
    model = Mailing
    permission_required = 'mailing.view_mailing'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.groups.filter(name="manager").exists():
            return qs
        return qs.filter(author=self.request.user)


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс детального представления рассылки"""
    model = Mailing
    permission_required = 'mailing.view_mailing'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return HttpResponseForbidden('У вас нет прав для просмотра этой страницы')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        mailing = Mailing.objects.get(pk=self.object.pk)
        recipients = mailing.recipients.all()
        context = super().get_context_data(**kwargs)

        context['recipients'] = recipients
        return context


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс создания рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")
    permission_required = 'mailing.add_mailing'

    def form_valid(self, form):
        mailing = form.save(commit=False)
        mailing.author = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Класс изменения рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")
    permission_required = 'mailing.change_mailing'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return HttpResponseForbidden('У вас нет прав для просмотра этой страницы')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse("mailing:mailing_detail", args=[self.kwargs.get('pk')])


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Класс удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")
    permission_required = 'mailing.delete_mailing'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return HttpResponseForbidden('У вас нет прав для просмотра этой страницы')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


def index(request):
    """Функция предтавления главной страницы"""

    mailings_all = MailingService.get_mailing()
    mailings_active = MailingService.get_mailing_active()
    client = MailingService.get_recipient()
    context = {
        'mailings_all': mailings_all,
        'mailings_active': mailings_active,
        'client': client
    }
    return render(request, 'mailing/index.html', context=context)


@permission_required('users.can_view_statistic', raise_exception=True)
def statistic_mailing(request, mailing_id):
    """Функция представления страницы статистики по рассылке"""

    mailing = get_object_or_404(Mailing, pk=mailing_id)
    if mailing.author != request.user:
        return HttpResponseForbidden('У вас нет прав для просмотра этой страницы')
    attempts = MailingAttempt.objects.filter(mailing_id=mailing_id)
    attempt_success = attempts.filter(status='Успешно')
    attempt_not_success = attempts.filter(status='Не успешно')

    context = {
        'mailing': mailing,
        'attempts': attempts,
        'attempt_success': attempt_success,
        'attempt_not_success': attempt_not_success,
    }
    return render(request, 'mailing/statistic.html', context=context)


@permission_required('users.can_send_mail', raise_exception=True)
def send_mail(request, mailing_id):
    """Функция отправки сообщения"""
    MailingService.send_mail(mailing_id)
    return render(request, 'mailing/send_ok.html')


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Класс представления рассылки"""
    model = User
    permission_required = 'users.manager'
    template_name = 'mailing/user_list.html'
    context_object_name = 'users'


@permission_required('users.manager', raise_exception=True)
def user_blocking(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    return render(request, 'mailing/user_block.html', {'user': user})


@permission_required('users.manager', raise_exception=True)
def user_unblocking(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()
    return render(request, 'mailing/user_unblock.html', {'user': user})


@permission_required('users.manager', raise_exception=True)
def mailing_blocking(request, mailing_id):
    mailing = Mailing.objects.get(pk=mailing_id)
    mailing.status = "Завершена"
    mailing.save()
    return render(request, 'mailing/mailing_block.html', {'mailing': mailing})


@permission_required('users.manager', raise_exception=True)
def mailing_unblocking(request, mailing_id):
    mailing = Mailing.objects.get(pk=mailing_id)
    mailing.status = "Запущена"
    mailing.save()
    return render(request, 'mailing/mailing_unblock.html', {'mailing': mailing})