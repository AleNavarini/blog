# Generated by Django 2.2.7 on 2019-12-12 00:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191211_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 21, 5, 30, 925470), verbose_name='Fecha de Publicacion'),
        ),
    ]