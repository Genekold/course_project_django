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
    """Класс объекта 'сообщение'"""

    subject = models.CharField(max_length=150, verbose_name="Тема сообщения", help_text="Тема")
    message = models.TextField(verbose_name="Тескт сообщения", help_text="Тескт сообщения")


class Mailing(models.Model):
    """Класс объекта 'рассылка'"""

    STATUS_CHOICES = [("Создана", "Создана"), ("Запущена", "Запущена"), ("Завершена", "Завершена")]

    start_date = models.DateTimeField(verbose_name="Дата и время первой рассылки")
    end_date = models.DateTimeField(verbose_name="Дата и время окончания рассылки")
    status = models.CharField(
        max_length=9, verbose_name="Статус рассылки", blank=True, null=True, choices=STATUS_CHOICES, default="Создана"
    )
    message = models.ForeignKey(Message, verbose_name="сообщение", on_delete=models.CASCADE, related_name="mailings")
    recipients = models.ManyToManyField(
        MailingRecipient, verbose_name="Получатели рассылки", related_name="recipients"
    )
