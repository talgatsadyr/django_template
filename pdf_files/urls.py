from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import files, create_files, file_detail, file_delete
from conf import settings

urlpatterns = [
    path('', files, name='files_list'),
    path('create_files/', create_files, name='create_files'),
    path('file/<int:id>', file_detail, name='file_detail'),
    path('file_delete/<int:id>', file_delete, name='file_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
