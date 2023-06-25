from django.urls import path
from .views import (
    ArticleCreateView,
    ArticlesListView,
    ArticleTemplateView,
    ArticleUpdateView,
    ArticleDeleteView
)
app_name = 'articles'
urlpatterns = [
    path('',ArticlesListView.as_view(),name='articles_view'),
    path('<int:pk>',ArticleTemplateView.as_view(),name='articles_view'),
    path('create', ArticleCreateView.as_view(), name='articles_create'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='articles_update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='articles_delete'),

]