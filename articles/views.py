from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.views.generic.base import TemplateView
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.

class ArticlesListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles_view.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['articles'] = []
    #     return context

class ArticleTemplateView(DetailView):
    model  = Article
    template_name = 'articles_detail.html'
    context_object_name = 'article'
    form_class = CommentForm
    success_url = reverse_lazy('articles:artciles_view')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['form'] = self.form_class
        context['comments'] = Comment.objects.filter(article = self.get_object())
    
        return context
    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            text=request.POST.get('text'),
            author = request.user,
            article=self.get_object(),
        )
        new_comment.save()


        return self.get(request, *args, **kwargs)
class ArticleCreateView(CreateView):
    template_name = 'articles_form.html'
    model = Article
    success_url = reverse_lazy('articles:articles_view')
    form_class = ArticleForm

class ArticleUpdateView(UpdateView):
    template_name = 'articles_form.html'
    model = Article
    success_url = reverse_lazy('articles:articles_view')
    form_class = ArticleForm

class ArticleDeleteView(DeleteView):
    template_name = 'articles_delete.html'
    model = Article
    success_url = reverse_lazy('articles:articles_view')
