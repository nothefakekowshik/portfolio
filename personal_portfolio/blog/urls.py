
from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'blog'
urlpatterns = [
    path('home',views.home,name='home'),
    path('allBlogs',views.all_blogs,name='allBlogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
]