from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.core.management import call_command

from users.models import User


class Command(BaseCommand):
    """Класс для пердварительной загрузки данных в базу данных"""

    def handle(self, *args, **options):
        user1 = User.objects.create(email='user1@mail.ru', is_active=True)
        user1.set_password('Qwe123')
        user1.save()
        user2 = User.objects.create(email='user2@mail.ru', is_active=True)
        user2.set_password('Qwe123')
        user2.save()
        moder = User.objects.create(email='moder@mail.ru', is_active=True)
        moder.set_password('Qwe123')
        moder.save()

        user_group = Group.objects.create(name='user')
        manager_group = Group.objects.create(name='manager')

        add_mailing = Permission.objects.get(codename='add_mailing')
        change_mailing = Permission.objects.get(codename='change_mailing')
        delete_mailing = Permission.objects.get(codename='delete_mailing')
        view_mailing = Permission.objects.get(codename='view_mailing')
        add_message = Permission.objects.get(codename='add_message')
        change_message = Permission.objects.get(codename='change_message')
        delete_message = Permission.objects.get(codename='delete_message')
        view_message = Permission.objects.get(codename='view_message')
        add_mailingrecipient = Permission.objects.get(codename='add_mailingrecipient')
        change_mailingrecipient = Permission.objects.get(codename='change_mailingrecipient')
        delete_mailingrecipient = Permission.objects.get(codename='delete_mailingrecipient')
        view_mailingrecipient = Permission.objects.get(codename='view_mailingrecipient')
        moderator = Permission.objects.get(codename='moderator')
        can_view_all_mailing = Permission.objects.get(codename='can_view_all_mailing')
        can_block_mailing = Permission.objects.get(codename='can_block_mailing')
        can_view_all_client = Permission.objects.get(codename='can_view_all_client')
        can_view_statistic = Permission.objects.get(codename='can_view_statistic')
        can_send_mail = Permission.objects.get(codename='can_send_mail')


        user_group.permissions.add(add_mailing, change_mailing, delete_mailing, view_mailing, add_message,
                                   change_message, delete_message, view_message, add_mailingrecipient,
                                   change_mailingrecipient, delete_mailingrecipient, view_mailingrecipient,
                                   can_view_statistic, can_send_mail)

        manager_group.permissions.add(view_mailing, view_message, view_mailingrecipient, can_block_mailing,
                                      can_view_all_mailing, moderator, can_view_all_client)

        user1.groups.add(user_group)
        user2.groups.add(user_group)
        moder.groups.add(manager_group)



        # call_command('loaddata', 'mailingrecipient_fixture.json')
        # call_command('loaddata', 'message_fixture.json')
        # call_command('loaddata', 'mailing_fixture.json')

        self.stdout.write(self.style.SUCCESS('Данные загружены'))
