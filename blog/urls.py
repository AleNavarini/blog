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
    path("login/", views.loginPage, name = "login"),
    path("register/", views.register, name = "register"),
    path("account/", views.account, name= "account"),
    path("logout/", views.user_logout, name= "logout"),
]
