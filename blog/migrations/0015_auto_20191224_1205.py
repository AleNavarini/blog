# Generated by Django 2.2.7 on 2019-12-24 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191223_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 24, 12, 5, 16, 607122), verbose_name='Fecha de Publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='viewCounter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
