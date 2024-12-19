from django.db import models


class MailingRecipient(models.Model):
    """Класс получателя рассылки"""

    email = models.EmailField(
        unique=True, help_text="email получателя рассылки", verbose_name="email получателя рассылки"
    )
    full_name = models.CharField(max_length=150, verbose_name="Ф.И.О. получателя", help_text="Ф.И.О. получателя")
    commentary = models.TextField(verbose_name="Комментарий о получателе рассылки", blank=True, null=True)

    def __str__(self):
        """Строковое представление получателя"""
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["full_name"]


class Message(models.Model):
    """Класс объекта сообщение"""

    subject = models.CharField(max_length=150, verbose_name="Тема сообщения", help_text="Тема")
    message = models.TextField(verbose_name="Тескт сообщения", help_text="Тескт сообщения")
