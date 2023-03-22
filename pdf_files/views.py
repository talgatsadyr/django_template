from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from pdf_files.models import Category, Files


def index(request):
    queryset = Category.objects.all()
    title = 'Список категорий'
    desc = 'Список категорий в базе данных'
    return render(request, 'main.html', {'title': title, 'desc': desc, 'queryset': queryset})


def files(request):
    queryset = Files.objects.all()
    title = 'Список файлов'
    if request.GET.get('search_box', None):
        search_text = request.GET.get('search_box', None)
        records = Files.objects.filter(title=search_text)
        return render(request, 'files_list.html', {'queryset': records, 'title': title})
    return render(request, 'files_list.html', {'queryset': queryset, 'title': title})

# Create your views here.
