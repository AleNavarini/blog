# Generated by Django 2.2.7 on 2019-12-12 00:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191211_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 21, 3, 23, 159183), verbose_name='Fecha de Publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
