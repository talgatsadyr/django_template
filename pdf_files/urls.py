from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, files

from conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('files/', files, name='files_list'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
