# Generated by Django 2.2.7 on 2019-12-12 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191211_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 21, 21, 59, 467656), verbose_name='Fecha de Publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitulo',
            field=models.TextField(),
        ),
    ]
