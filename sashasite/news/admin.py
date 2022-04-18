from django.contrib import admin
from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)   # тюпл, а не строка
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)          # тюпл, а не строка


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
