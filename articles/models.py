from tabnanny import verbose
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
# Create your models here.
 
class Article(models.Model):
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=150)
    slug = models.SlugField(verbose_name='slug', blank=True)
    text = models.TextField(verbose_name='Контент',blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to= 'articles/')
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Изменено', auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Cтатьи'
        ordering = ['created_at', ]

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.title = slugify(_(self.title))
        super(Article, self).save(*args, **kwargs) 
        
class Comment(models.Model):
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, default=1)
    text = models.TextField(verbose_name='Комментарий', blank=True)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at',]

    def __str__(self):
        return f'{self.author.username}- {self.text[:40]}'
