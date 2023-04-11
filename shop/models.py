from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class CategorySeason(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_season_name')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сезоны'
        verbose_name_plural = 'Сезон'


class CategorySize(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_size_name')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размеры'
        verbose_name_plural = 'Размер'


class Product(models.Model):
    title = models.CharField(verbose_name='Название товара', max_length=255, blank=True)
    season = models.ForeignKey(CategorySeason, verbose_name='Сезон', on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(CategorySize, verbose_name='Размер', on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена товара', default=0)
    text = RichTextField('Описание', null=True, blank=True)
    link = models.URLField(verbose_name='Ссылка', null=True, blank=True)

    image = models.ImageField(verbose_name='Фото товара', upload_to='uploads', null=True, blank=True)
    download_image = models.FileField(upload_to='uploads', blank=True, null=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    pubdate = models.DateTimeField('Время создания товара', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.author, self.title)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

