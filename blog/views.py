from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from blog.models import Post, PageCounter

from django.db.models import Q

counter = 0
class YearlyPosts:
    year = ""
    posts = []

    def __init__(self, year, posts):
        self.year = year
        self.posts = posts

def homepage(request):
    pageCounter = PageCounter.objects.all()[0]
    pageCounter.counter += 1
    pageCounter.save()
    posts = Post.objects.all
   
    posts = Post.objects.filter().order_by('-id')[:3]
    postsPopular = Post.objects.filter().order_by('-viewCounter')[:3]

    years = []
    for p in posts:
        if p.fecha.year not in years:
            years.append(p.fecha.year)
    postsByYear = []
    for year in years:
        postsByYear.append(YearlyPosts(year, [p for p in posts if p.fecha.year == year]))

    return render(request,
                  "blog/home.html",
                  {"posts": posts,
                   "mostpopular" : postsPopular,
                   "counter":pageCounter,
                   "postsByYear": postsByYear})

def bio(request):

    return render(request,
                  "blog/bio.html")


def articulos(request):
    posts = Post.objects.all
   
    posts = Post.objects.filter().order_by('-id')
    return render(request,
                  "blog/articulos.html",
                  {"posts": posts})

def search(request):
    
    search = request.GET.get('search')
    if search == '':
        return homepage(request)	

    posts = Post.objects.filter(Q(contenido__contains = search) | Q(titulo__contains = search) | Q(subtitulo__contains = search) | Q(fecha__contains = search) | Q(autor__contains = search))
    posts = posts.order_by('-fecha')
    postsPopular = Post.objects.filter().order_by('-viewCounter')[:3]
    pageCounter= PageCounter.objects.all()[0]

    return render(request,
                "blog/home.html",
                {"posts": posts,
                "mostpopular" : postsPopular,
                "counter":pageCounter})

def post(request):
    
    postid = request.GET.get('post')
    post = Post.objects.get(pk = postid)
    post.viewCounter += 1
    post.save()

    return render(request, "blog/articulo.html", context = {"post": post})

def sobre(request):
    return render(request, "blog/sobre.html")