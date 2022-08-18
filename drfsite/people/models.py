from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class People(models.Model):
    title = models.CharField(max_length=50, verbose_name='Имя')
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'People'
        verbose_name_plural = 'Peoples'
        ordering = ['-time_create', 'title']


# ------------------------------------------------------------------------------------------

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']
