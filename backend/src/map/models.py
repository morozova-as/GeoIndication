from django.db import models

choicesStatus = [('Действует', 'Действует'),
                 ('Прекратил действие', 'Прекратил действие'),
                 ('Нет данных', 'Нет данных'),
                 ('Срок действия истек', 'Срок действия истек')]

choicesType = [('Другое', 'Другое'),
               ('Народные изделия', 'Народные изделия'),
               ('Напитки', 'Напитки'),
               ('Алкогольные напитки', 'Алкогольные напитки'),
               ('Продукты питания', 'Продукты питания')]


class GeoIndication(models.Model):
    id = models.AutoField(primary_key=True)
    href = models.TextField()
    status = models.TextField(choices=choicesStatus)
    name = models.TextField()
    description = models.TextField()
    geo_loc_original = models.TextField()
    target = models.TextField(choices=choicesType, null=True, blank=True)
    # original = models.IntegerField()
    # geo_loc_keywords = models.TextField(null=True, blank=True)
    geo_loc_polygon = models.TextField(null=True, blank=True)


class Manufacturers(models.Model):
    id = models.TextField(primary_key=True)
    mainId = models.ForeignKey(GeoIndication, on_delete=models.CASCADE)
    href = models.TextField()
    status = models.TextField(choices=choicesStatus)
    # name = models.TextField()
    description = models.TextField()
    # geo_loc_original = models.TextField(blank=True, null=True)
    manufacturer = models.TextField()
