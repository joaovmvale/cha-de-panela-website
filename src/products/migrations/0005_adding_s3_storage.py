# Generated by Django 4.0.2 on 2022-03-01 16:34

import core.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_changing_logical_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', storage=core.storage_backends.PublicMediaStorage, upload_to='products/images/', verbose_name='Imagem do produto'),
        ),
    ]