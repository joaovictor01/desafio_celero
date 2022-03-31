"""desafio_celero URL Configuration"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from desafio_celero import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('desafio_celero.api_urls')),
    path('olympics/', include('olympics.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
