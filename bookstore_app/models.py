from django.conf import settings
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Кем добавлен')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Кем добавлена')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.title
