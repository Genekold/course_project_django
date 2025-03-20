
from django.core.management.base import BaseCommand

from mailing.services import MailingService


class Command(BaseCommand):
    help = 'Команда для запуска рассылок вручную'

    def handle(self, *args, **options):

        try:
            mailing_pk = int(input('Введите номер рассылки: '))
        except ValueError:
            print('Введено не числовое значение!')
            return None

        MailingService.send_mail(mailing_pk)

