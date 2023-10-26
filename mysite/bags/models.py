from django.db import models
from django.urls import reverse


class Bags(models.Model):
    title = models.CharField(max_length=150, verbose_name='Бренд')
    description = models.TextField(blank=True, verbose_name='Опис')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус публікації')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категорія',)
    views=models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_bag', kwargs={'pk': self.pk})

    def my_func(self):
        return 'hello from model'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сумочка'
        verbose_name_plural = 'Сумочки'
        ordering = ['-added_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']
