from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls import url

app_name = "blog"

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    re_path("bio/", views.bio, name = "bio"),
    re_path("sobre/", views.sobre, name = "sobre"),
    re_path("articulos/", views.articulos, name = "articulos"),
    re_path(r'search/$' , views.search ,name= "search"),
    re_path(r'posts/$',views.post, name = 'post'),
    re_path("login/", views.login, name = "login"),
    re_path("register/", views.register, name = "register"),
    re_path(r"validateLogin/", views.validateLogin, name= "validateLogin"),
    re_path(r"user/", views.createUser, name= "createUser"),   
]
