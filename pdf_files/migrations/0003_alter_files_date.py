# Generated by Django 4.1.7 on 2023-06-14 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_files', '0002_files_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 21, 16, 29, 587575)),
        ),
    ]
