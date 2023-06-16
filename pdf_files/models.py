
import os
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from users.models import User


class Category(MPTTModel):
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,verbose_name="Родитель",
                            null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Список Категорий'


class Files(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,
                                 null=True, blank=True, related_name='files')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files', null=True, blank=True)
    cover = models.ImageField(verbose_name='Обложка файла', upload_to='cover/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return f'{self.title}'

#
