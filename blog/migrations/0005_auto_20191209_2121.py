# Generated by Django 2.2.7 on 2019-12-10 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191209_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 21, 21, 33, 46171), verbose_name='Fecha de Publicacion'),
        ),
    ]
