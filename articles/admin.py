from re import A
from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk',]
admin.site.register(Article,ArticleAdmin)