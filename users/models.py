from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars//%Y/%m/%d/', verbose_name='Аватвр', blank=True, null=True)

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользоатель'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('can_view_statistic', 'can view statistic'),
            ('can_send_mail', 'can sand mail'),
            ('manager', 'manager'),
        ]

    def __str__(self):
        return self.email
