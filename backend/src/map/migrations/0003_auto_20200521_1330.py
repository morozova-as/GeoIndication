# Generated by Django 3.0.5 on 2020-05-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20200521_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoindication',
            name='target',
            field=models.TextField(blank=True, choices=[('Другое', 'Другое'), ('Народные изделия', 'Народные изделия'), ('Напитки', 'Напитки'), ('Алкогольные напитки', 'Алкогольные напитки'), ('Продукты питания', 'Продукты питания')], null=True),
        ),
    ]
