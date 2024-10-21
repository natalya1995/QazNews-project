from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_page, name='home_page'),
    path('news/all/',views.all_news_page, name='all_news_page'),
    path('news/detail/<int:pk>/',views.news_detail_page, name='news_detail_page'),
    path('news/tag/<slug:slug>/',views.tags_news_page, name='tags_news_page'),
    path('news/search/',views.search_page, name='search_page'),
    path('news/search/results/',views.search_results_page, name='search_results_page'),
]