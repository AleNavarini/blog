from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from blog.models import Post
from django.db.models import Q

def homepage(request):
    posts = Post.objects.all
   
    posts = Post.objects.filter().order_by('-id')[:6]
    return render(request,
                  "blog/home.html",
                  {"posts": posts,
                   "mostpopular" : posts})

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

def search(request):
    
	search = request.GET.get('search')
	if search == '':
		return homepage(request)	

	posts = Post.objects.filter(Q(contenido__contains = search) | Q(titulo__contains = search) | Q(subtitulo__contains = search) | Q(fecha__contains = search) | Q(autor__contains = search))
	posts = posts.order_by('-fecha')

	return render(request, "blog/home.html" , context = { "posts" : posts } )

def post(request):
    
	postid = request.GET.get('post')
	post = Post.objects.get(pk = postid)

	return render(request, "blog/articulo.html", context = {"post": post})