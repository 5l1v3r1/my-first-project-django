from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [

    path('', index_view, name="blog_index_url"),
    path('search/', search_article, name="search_article"),

    path('reviews/', reviews_list, name="reviews_list_url"),
    path('reviews/new/', review_new, name="review_new_url"),

    path('contacts/', contacts_view, name="contacts_url"),

    path('<str:category_slug>/', list_artcles, name="list_articles_url"),
    path('<str:category_slug>/<str:article_slug>/', detail_article, name="detail_article_url"),

]
