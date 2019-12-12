from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from blog.models import Post

def homepage(request):

    return render(request,
                  "blog/home.html",
                  {"posts": Post.objects.all})

def bio(request):

    return render(request,
                  "blog/bio.html")

def colaboraciones(request):

    return render(request,
                  "blog/colab.html",
                  )

def articulos(request):

    return render(request,
                  "blog/home.html",
                  {"posts": Post.objects.all})

def buscaArticulos(request):
    
    search = request.GET.get('search')
    post = Post.objects.get(pk = postid)
	
    return render(request, "main/buscaArticulos.html",context = {"post": post})