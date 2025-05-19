import datetime
import smtplib

from django.core.cache import cache
from django.core.mail import send_mail

from config.settings import DEFAULT_FROM_EMAIL
from .models import Mailing, MailingRecipient, MailingAttempt


class MailingService:

    @staticmethod
    def data_update():
        """Обновление данных в базе данных в зависимости от даты окончания рассылки """
        mailings = Mailing.objects.all()
        for mailing in mailings:
            if mailing.end_date.replace(tzinfo=None) < datetime.datetime.now():
                mailing.status = 'Завершена'
                mailing.save()


    @staticmethod
    def send_mail(mailing_pk):
        """Mетод для отправки сообщений"""

        mailing = Mailing.objects.get(pk=mailing_pk)
        subject = mailing.message.subject
        text = mailing.message.message
        recipients = [rec.email for rec in mailing.recipients.all()]
        for recipient in recipients:
            try:
                if mailing:
                    send_mail(subject=subject, message=text, recipient_list=recipients, from_email=DEFAULT_FROM_EMAIL)
                    message_server = f"Сообщение успешно отправлено {recipient}"
                    print(message_server)
                    MailingAttempt.objects.create(status='Успешно', server_response=message_server, mailing=mailing)
                else:
                    print('Нет такой рассылки')
            except smtplib.SMTPException as e:
                message_server = f'Собщение клиненту {recipient} не отправлено. Ошибка {str(e)}'
                MailingAttempt.objects.create(status='Не успешно', server_response=message_server, mailing=mailing)
                print(e)

    @staticmethod
    def get_mailing():
        """Получение всех рассылок для главной страницы"""

        mailings_all = cache.get('mailings_all')
        if not mailings_all:
            mailings_all = Mailing.objects.all()
        return mailings_all

    @staticmethod
    def get_mailing_active():
        """Получение рассылок со статусом 'Запущена' для главной страницы"""

        mailings_active = cache.get('mailings_active')
        if not mailings_active:
            mailings_active = Mailing.objects.filter(status='Запущена')
        return mailings_active

    @staticmethod
    def get_recipient():
        """Получене всех уникальных получателей рассылки"""

        client = cache.get('clients')
        if not client:
            client = MailingRecipient.objects.values('email').distinct()
        return client
