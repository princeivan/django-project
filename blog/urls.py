from django.urls import path

from . import views

app_name = 'blog'

urlpatterns =[
    path('', views.blog_post_list ),
    path('<str:slug>/', views.blog_post_detail ),
    path('<str:slug>/edit', views.blog_post_update ),
    path('<str:slug>/delete/', views.blog_post_delete ),

]