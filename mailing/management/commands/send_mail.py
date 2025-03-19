from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from config.settings import DEFAULT_FROM_EMAIL
from mailing.models import Mailing

Exception
class Command(BaseCommand):
    help = 'Команда для запуска рассылок вручную'

    def handle(self, *args, **options):

        try:
            mailing_pk = int(input('Введите номер рассылки: '))
        except ValueError:
            print('Введено не числовое значение!')
            return None

        mailing = Mailing.objects.filter(pk=mailing_pk).first()

        if mailing:
            subject = mailing.message.subject
            text = mailing.message.message
            recipients = [rec.email for rec in mailing.recipients.all()]
            send_mail(subject=subject, message=text, recipient_list=recipients, from_email=DEFAULT_FROM_EMAIL)
            print("Сообщение отправлено")
        else:
            print('Нет такой рассылки')

