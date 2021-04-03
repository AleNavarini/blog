from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from blog.models import Post, PageCounter, CarrImage, User
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


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
    allPosts = Post.objects.filter().order_by('-fecha')
    years = []
    for p in allPosts:
        if p.fecha.year not in years:
            years.append(p.fecha.year)
   
    posts = Post.objects.filter().order_by('-id')[:3]
    postsPopular = Post.objects.filter().order_by('-viewCounter')[:3]


    postsByYear = []
    for year in years:
        postsByYear.append(YearlyPosts(year, [p for p in allPosts if p.fecha.year == year]))

    carrImages = CarrImage.objects.filter()

    return render(request,
                  "blog/home/home.html",
                  {"posts": posts,
                   "mostpopular" : postsPopular,
                   "counter":pageCounter,
                   "postsByYear": postsByYear,
                   "carrImages": carrImages,})

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
    allPosts = Post.objects.filter().order_by('-fecha')
    years = []

    postsByYear = []
    for year in years:
        postsByYear.append(YearlyPosts(year, [p for p in allPosts if p.fecha.year == year]))

    carrImages = CarrImage.objects.filter()
    return render(request,
                  "blog/home/home.html",
                  {"posts": posts,
                   "mostpopular" : postsPopular,
                   "counter":pageCounter,
                   "postsByYear": postsByYear,
                   "carrImages": carrImages,})

def post(request):
    
    postid = request.GET.get('post')
    post = Post.objects.get(pk = postid)
    post.viewCounter += 1
    post.save()

    return render(request, "blog/articulo.html", context = {"post": post})

def sobre(request):
    return render(request, "blog/sobre.html")


def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid:
            print(form)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username, password= password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Inicaste sesion como {username}! ")
                return redirect("blog:homepage")
            else:
                messages.error(request, "Ha habido un error al iniciar sesion")
        
    
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request,
                    "blog/login.html",
                    context= {"form" : form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f" Registrado exitosamente!")
            login(request, user)
            return redirect("blog:homepage")
        else:
            for m in form.error_messages:
                messages.error(request, "Ha habido un problema con el registro, revise los campos y vuelva a intentar")
            return redirect("blog:homepage")
    
    if request.method == "GET":
        form = UserCreationForm()
        return render(request,
                    "blog/register.html",
                    context= {"form" : form})

def account(request):
    return render(request, "blog/account.html")

def user_logout(request):
    logout(request)
    return redirect("blog:homepage")



