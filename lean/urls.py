from . import views
from django.conf.urls import url
from django.urls import path, re_path

urlpatterns = [
    path('',views.index, name='index'),
    path('posts',views.post_display, name='post_display'),
    path('articles/blogs',views.article_add, name='article_add'),
    path('articles',views.blog_display, name='blog_display'),
    path('listing',views.location_disp, name='loaction_disp'),
    path('listing/delhi',views.delhi_add, name='delhi_add'),
    path('listing/bangalore',views.bangalore_add, name='bangalore_add'),
    path('listing/chennai',views.chennai_add, name='chennai_add'),
    path('listing/mumbai',views.mumbai_add, name='mumbai_add'),
    path('questions',views.ques_disp, name="ques_disp"),
    path('questions/add_ques',views.ques_add, name="ques_add"),
    path('home',views.home_disp, name="home_disp"),
]