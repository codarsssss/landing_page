from django.db import models


# Модель заявок
class Consultation(models.Model):
    class Status(models.TextChoices):
        CALLED_BACK = 'ДА', 'ПЕРЕЗВОНИЛИ'
        NO_CALLED_BACK = 'НЕТ', 'НЕ ПЕРЕЗВОНИЛИ'

    username = models.CharField(max_length=100, verbose_name='Имя')
    number = models.CharField(max_length=12, verbose_name='Номер телефона')
    status = models.CharField(max_length=3, choices=Status.choices,
                              default=Status.NO_CALLED_BACK, verbose_name='Статус')
    date_application = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    class Meta:
        ordering = ['-date_application']

        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.username
