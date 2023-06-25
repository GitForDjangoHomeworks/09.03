
from django import forms

from .models import Article, Comment
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'text', 'image', 'title']

        widgets = {
                'author' : forms.Select(attrs={
                    'class': "form-control",
                    'style': 'max-width: 300px;'}),
                'title': forms.TextInput(attrs={'class': 'form-control', 
                                                'placeholder': 'Заголовок статьи', 
                                                'required': 'required'}),
                'image': forms.FileInput(attrs={'class': 'form-control', 'label': 'Изображение'}),
                'text': forms.Textarea(attrs={  'class': 'form-control', 
                                                'required': 'required',
                                                'placeholder': 'Оставьте Ваш отзыв'
                                                    }),
                
            }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text']
        labels = {
            'text' : 'Комментарий',
        }
        widgets = {
                'text': forms.Textarea(attrs={'class': 'form-control', 
                                                'placeholder': 'Введите коментарий', 
                                                'required': 'required'}),
                }
                                                
                                                
                