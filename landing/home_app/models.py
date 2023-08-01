from django.db import models

# Create your models here.

# Модель услуг
class Service(models.Model):

    title = models.CharField(max_length=255, verbose_name='Наименование услуги',
                             blank=False)
    description = models.CharField(max_length=255, verbose_name='Краткое описание',
                                   blank=False)
    price = models.IntegerField(verbose_name='Стоимость услуги', default=0,
                                blank=False)
    active = models.BooleanField(default=1, verbose_name='Активна/Не активна')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    class Meta:
        verbose_name_plural = 'Услуги'
        ordering = ['-create_date']


    def __str__(self):
        return self.title
    

# Модель отзывов
class Review(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email', blank=True)
    body = models.TextField(verbose_name='Текст отзыва')
    create_date = models.DateTimeField(verbose_name='Дата создания')
    active = models.BooleanField(default=1, verbose_name='Активные/Не активный')


    class Meta:
        verbose_name_plural = 'Отзывы'
        ordering = ['-create_date']

    
    def __str__(self):
        return self.name


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