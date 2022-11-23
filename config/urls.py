from django.contrib import admin
from django.urls import path,include
from blog.views import iletisim
from django.conf.urls.static import static #debug modda otomotik url ptterni olusuturuyo 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
