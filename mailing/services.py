import smtplib

from django.core.mail import send_mail

from config.settings import DEFAULT_FROM_EMAIL
from .models import Mailing, MailingRecipient, MailingAttempt, Message


class MailingService:

    @staticmethod
    def send_mail(mailing_pk):
        """Mетод для отправки сообщений"""

        mailing = Mailing.objects.filter(pk=mailing_pk).first()
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
        return Mailing.objects.all()

    @staticmethod
    def get_mailing_active():
        return Mailing.objects.filter(status='Запущена')

    @staticmethod
    def get_recipient():
        return MailingRecipient.objects.all()