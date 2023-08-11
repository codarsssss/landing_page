from django.db import models
from django.db.models.query import QuerySet


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
        ordering = ['-create_date']

        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


def review_photo_path(instance, filename):
    return 'review_photo/id_{}/{}'.format(instance.pk, filename)


# Модель отзывов
class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    body = models.TextField(verbose_name='Текст отзыва')
    image = models.ImageField(verbose_name='Фото', upload_to=review_photo_path, blank=True)
    create_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата создания')
    active = models.BooleanField(default=1, verbose_name='Активные/Не активный')

    class Meta:
        ordering = ['-create_date']

        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


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


# Создаёт путь, по которому будет находиться фото новости
# Указание slug позволит скрипту быстрее находить нужный файл
def news_photo_path(instance, filename):
    return 'news_photo/slug_{}/{}'.format(instance.slug, filename)


"""

class NewsPublishedManager(models.Manager) является конкретно-прикладным 
модельным менеджером, в конкретном случае он будет выводить из бд 
только те посты, у которых есть статут 'Опубликован'.  
Для извлечения обектов нужно использовать 'News.published.all()'.

Если вы хотите использовать кастомный модельный менеджер и при этом
сохранить стандартный 'News.objects.all()', то нужно его явно указать
перед кастомным - 1) objects = models.Manager() 2) published = NewsPublishedManager().
Также можно использовать Meta-атрибут default_manager_name.

"""


class NewsPublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(
            status=News.Status.PUBLISHED)


# Модель новостей
class News(models.Model):
    class Status(models.TextChoices):
        NOT_PUBLISHED = 'Нет', 'Не опубликована'
        PUBLISHED = 'Да', 'Опубликована'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='Слаг поста')
    image = models.ImageField(verbose_name='Фото', upload_to=news_photo_path, blank=True)
    text = models.TextField(verbose_name='Текст новости')
    status = models.CharField(verbose_name='Статус', max_length=3,
                              choices=Status.choices, default=Status.NOT_PUBLISHED)
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    objects = models.Manager()  # Менеджер, применяемый по умолчанию
    published = NewsPublishedManager()  # Конкретно-прикладной менеджер

    class Meta:
        ordering = ['-create_datetime']

        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
