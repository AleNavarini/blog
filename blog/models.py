from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length = 200)
    subtitulo = models.TextField()
    autor = models.CharField(max_length = 200)
    contenido = models.TextField()
    fecha = models.DateTimeField("Fecha de Publicacion", default = datetime.now() )
    
    foto = models.ImageField(blank = True, null = True)
    viewCounter = models.IntegerField(blank = True, null = True, default = 0)

    def __str__(self):
        return self.titulo
    
    def getYear(self):
        return fecha.year

class PageCounter(models.Model):
    counter = models.IntegerField()

class CarrImage(models.Model):
    image = models.URLField(default= r"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.formulad.org%2Fes%2Fphotogalleries%2F2017-08-09-gallery-not-found%2F&psig=AOvVaw1sNW9BAEhcHcDtmF-wvnm4&ust=1617411070167000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLis6vir3u8CFQAAAAAdAAAAABAD")
    desc_alternativa = models.CharField(max_length = 200)

class User(models.Model):
    username = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    mail = models.CharField(max_length = 200)