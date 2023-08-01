from django.db import models


class Consultation(models.Model):

    class Status(models.TextChoices):
        CALLED_BACK = 'ДА', 'ПЕРЕЗВОНИЛИ'
        NO_CALLED_BACK = 'НЕТ', 'НЕ ПЕРЕЗВОНИЛИ'
    username = models.CharField(max_length=100)
    number = models.CharField(max_length=12)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.NO_CALLED_BACK)
    date_application = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_application']
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.username


class News(models.Model):

    title = models.CharField(max_length=255)
    slug = models.URLField()
    image = models.ImageField()
    text = models.TextField()
    create_datetime = models.DateTimeField(auto_now_add=True)

    def Meta:
    ordering = ['-create_datetime']

    def __str__(self):
        return self.title