from django.db import models


class MailingRecipient(models.Model):
    """Класс получателя рассылки"""

    email = models.EmailField(
        unique=True, verbose_name="email получателя рассылки"
    )
    full_name = models.CharField(max_length=150, verbose_name="Ф.И.О. получателя")
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

    subject = models.CharField(max_length=150, verbose_name="Тема сообщения")
    message = models.TextField(verbose_name="Тескт сообщения")

    def __str__(self):
        """Строковое представление сообщения"""
        return f"{self.subject}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["subject"]


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

    def __str__(self):
        """Строковое представление рассылки"""
        return f"{self.message} статус рассылки {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["status"]


class MailingAttempt(models.Model):
    """Класс попытки рассылки"""

    STATUS_ATTEMPT = [('Успешно', 'Успешно'), ('Не успешно', 'Не успешно')]

    date_attempt = models.DateTimeField(verbose_name='Дата и время попытки', auto_now_add=True)
    status = models.CharField(verbose_name='Успешность отправки', choices=STATUS_ATTEMPT)
    server_response = models.TextField(verbose_name='Ответ почтового сервера')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', related_name='attempt')

    def __str__(self):
        return f'{self.pk} | {self.date_attempt} | {self.status}'

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"

