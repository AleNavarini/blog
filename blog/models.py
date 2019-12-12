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

    def __str__(self):
        return self.titulo
