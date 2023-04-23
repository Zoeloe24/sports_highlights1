from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-featured-videos', views.allFeaturedVideos, name='allFeaturedVideos'),
    path('all-popular-videos', views.allPopularVideos, name='allPopularVideos'),
    path('article_details/<str:pk>/', views.articleDetails, name='articleDetails'),
    path('all-articles', views.allArticles, name='allArticles'),

    path('success-page/', views.successPage, name='successPage'),
]