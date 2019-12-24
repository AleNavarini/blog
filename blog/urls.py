from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls import url

app_name = "blog"

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    re_path("bio/", views.bio, name = "bio"),
    re_path("colaboraciones/", views.colaboraciones, name = "colab"),
    re_path("articulos/", views.articulos, name = "articulos"),
    re_path(r'search/$' , views.search ,name= "search"),
    re_path(r'posts/$',views.post, name = 'post'),
 
    
]
