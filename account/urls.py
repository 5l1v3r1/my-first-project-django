from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('', index_view, name="index_url"),

    path('search/', search_in_articles, name="admin_search_article_url"),

    path('contacts/edit/', contacts_edit, name="admin_contacts_edit"),
    path('contacts/<str:contacts_id>/update/', contacts_update, name="admin_update_contacts_url"),

    path('category/create/', category_create, name="admin_category_create_url"),
    path('category/save/', category_save, name="admin_category_save_url"),
    path('category/<str:category_id>/update/', update_category, name="admin_update_category_url"),
    path('category/<str:category_id>/edit/', edit_category, name="admin_edit_category_url"),
    path('category/<str:category_id>/delete/', category_delete, name="admin_category_delete_url"),
    path('category/<str:category_slug>/', category_view_article, name="admin_category_article_list_url"),

    path('article/create/', create_article, name="admin_create_article_url"),
    path('article/save/', save_article, name="admin_save_article_url"),
    path('article/<str:article_id>/update/', update_article, name="admin_update_article_url"),
    path('article/<str:article_id>/edit/', edit_article, name="admin_edit_article_url"),
    path('article/<str:article_id>/delete/', delete_article, name="admin_category_article_delete_url"),

    path('static_information/<str:info_id>/edit/', static_information_edit, name="admin_static_information_edit_url"),
    path('static_information/<str:info_id>/update/', static_information_update, name="admin_update_static_info_url"),

    path('reviews/', reviews_list, name="admin_reviews_list_url"),
    path('reviews/create/', review_create, name="admin_create_review_url"),
    path('reviews/save/', review_save, name="admin_review_save_url"),
    path('reviews/<str:review_id>/edit/', review_edit, name="admin_edit_review_url"),
    path('reviews/<str:review_id>/update/', review_update, name="admin_update_review_url"),
    path('reviews/<str:review_id>/delete/', review_delete, name="admin_delete_review_url"),

    path('main-slider/', main_slider_list, name="admin_main_slider_list_url"),
    path('main-slider/create/', main_slider_create, name="admin_create_slider_url"),
    path('main-slider/save/', main_slider_save, name="admin_save_slider_url"),
    path('main-slider/<str:slider_id>/edit/', main_slider_edit, name="admin_edit_slider_url"),
    path('main-slider/<str:slider_id>/update/', main_slider_update, name="admin_update_slider_url"),
    path('main-slider/<str:slider_id>/delete/', main_slider_delete, name="admin_delete_slider_url"),

    path('main-page/edit/', main_page_edit, name="admin_edit_main_page_url"),
    path('main-page/<str:mpage_id>/update/', main_page_update, name="admin_update_main_page_url")
]
