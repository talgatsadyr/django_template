from django import forms
from pdf_files.models import Category, Files


class FilesCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Заголовок файла")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория файла', required=False)
    file = forms.FileField(widget=forms.FileInput, label='Файл')
    cover = forms.ImageField(label='Обложка')
    description = forms.CharField(label='Описание', widget=forms.Textarea)

    class Meta:
        model = Files
        fields = ('title', 'category', 'file', 'cover')
