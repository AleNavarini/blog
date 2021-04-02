from django.contrib import admin
from blog.models import *
from tinymce.widgets import TinyMCE
from django.db import models

class PostAdmin(admin.ModelAdmin):

   

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Post,PostAdmin)
admin.site.register(PageCounter)
admin.site.register(CarrImage)