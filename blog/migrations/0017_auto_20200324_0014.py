# Generated by Django 2.2.10 on 2020-03-24 03:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200126_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarrImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc_alternativa', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 0, 14, 32, 524231), verbose_name='Fecha de Publicacion'),
        ),
    ]
