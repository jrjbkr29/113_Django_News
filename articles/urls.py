from django.urls import path
from .views import ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView, ArticleCreateView, ArticleCommentView

# 127.0.0.1:8000/articles/[url paths from below]
# articles/id/edit/ --> users can modify
# articles/id/delete/ --> users can remove article
# articles/id/edit/ --> users can modify

urlpatterns = [
    path('', ArticleListView.as_view(), name= 'article_list'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new', ArticleCreateView.as_view(), name='article_new'),
    path('comment', ArticleCommentView.as_view(), name='comment_new'),
]