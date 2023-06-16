from django.shortcuts import render, redirect

from pdf_files.forms import FilesCreateForm
from pdf_files.models import Files
from django.http import HttpResponse
from django.db.models import Q


def files(request):
    queryset = Files.objects.all()
    title = 'Список файлов'
    if request.GET.get('search_box', None):
        search_text = request.GET.get('search_box', None)
        records = Files.objects.filter(Q(title__contains=search_text) | Q(category__contains=search_text))
        return render(request, 'files_list.html', {'queryset': records, 'title': title})
    return render(request, 'files_list.html', {'queryset': queryset, 'title': title})


def create_files(request):
    if request.user.user_status == 'simple':
        return HttpResponse('У вас недостаточно прав для этой операции')
    else:
        if request.method == 'POST':
            form = FilesCreateForm(request.POST)
            form.is_valid()
            Files.objects.create(title=form.cleaned_data.get('title', ''),
                                 category=form.cleaned_data.get('category', None),
                                 file=request.POST.get('file', None),
                                 cover=request.POST.get('cover', None),
                                 user=request.user)
            return HttpResponse('Успешно создано')
        else:
            form = FilesCreateForm()
            return render(request, 'files_create.html', {'form': form})


def file_detail(request, *args, **kwargs):
    file = Files.objects.get(id=kwargs['id'])
    if file.user.pk == request.user.pk:
        owner = True
    else:
        owner = False
    return render(request, 'file_detail.html', {'file': file, 'owner': owner})


def file_delete(request, *args, **kwargs):
    file = Files.objects.get(id=kwargs['id'])
    file.delete()
    return render(request, 'file_delete.html')



