from django.contrib import admin

from pdf_files.models import Category, Files


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = list_display


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = list_display
# Register your models here.
