from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from blog.models import Post

def homepage(request):

    return render(request,
                  "blog/master.html",
                  {"posts": Post.objects.all})