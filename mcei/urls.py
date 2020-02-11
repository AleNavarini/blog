from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from mcei import settings

urlpatterns = [
    path('',include('blog.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
