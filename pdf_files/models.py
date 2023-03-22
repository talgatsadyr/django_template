import datetime
import os

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


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
    date = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return f'{self.title}'

# Create your models here.
