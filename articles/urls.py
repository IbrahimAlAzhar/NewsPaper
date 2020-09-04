from django.urls import path
from . import views
# from .views import post_detail

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),
    #path('<int:my_id>/', post_detail, name='article_detail'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(),name='article_delete'),
]
