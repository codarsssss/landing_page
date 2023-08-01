from django.db import models


# Модель услуг
class Service(models.Model):

    title = models.CharField(max_length=255, verbose_name='Наименование услуги')
    description = models.CharField(max_length=255, verbose_name='Краткое описание')
    price = models.IntegerField(verbose_name='Стоимость услуги', default=0)
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
    email = models.EmailField(verbose_name='Email')
    body = models.TextField(verbose_name='Текст отзыва')
    create_date = models.DateTimeField(verbose_name='Дата создания')
    active = models.BooleanField(default=1, verbose_name='Активные/Не активный')


    class Meta:
        verbose_name_plural = 'Отзывы'
        ordering = ['-create_date']

    
    def __str__(self):
        return self.name


