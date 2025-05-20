from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views


app_name = 'main'
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('second', secondpage, name="secondpage"),
    path('new-post', new_post, name="new-post"),
    path('create', create, name="create"),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('mypage/', views.mypage, name='mypage'),
    path('tag-list', tag_list, name="tag-list"),
    path('tag-posts/<int:tag_id>', tag_posts, name="tag-posts"),

]
