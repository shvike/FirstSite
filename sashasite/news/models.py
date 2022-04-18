from django.db import models
from django.urls import reverse    # <<<


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Утверждено?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,
                             verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})  # <<< первый параметр viewname=названию маршрута (из urls.py  берем path('category/<int:category_id>/', get_category, name='category')); второй параметр - словарь с ключом category_id (см.входящие параметры в views.py, функция get_category(request, category_id) и значением=атрибутом модели id=pk). Благодаря этому методу джанго сам выстраивает ссылку.


    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
