from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Класс для пердварительной загрузки данных в базу данных"""

    def handle(self, *args, **options):
        call_command('loaddata', 'mailingrecipient_fixture.json')
        call_command('loaddata', 'message_fixture.json')
        call_command('loaddata', 'mailing_fixture.json')
        self.stdout.write(self.style.SUCCESS('Данные загружены'))
