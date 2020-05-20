from django.db import models


class GeoIndication(models.Model):
    id = models.IntegerField(primary_key=True)
    href = models.TextField()
    status = models.TextField()
    name = models.TextField()
    description = models.TextField()
    geo_loc_original = models.TextField()
    target = models.TextField()
    original = models.IntegerField()
    geo_loc_keywords = models.TextField()
    geo_loc_polygon = models.TextField()


class Manufacturers(models.Model):
    id = models.TextField(primary_key=True)
    mainId = models.ForeignKey(GeoIndication, on_delete=models.CASCADE)
    href = models.TextField()
    status = models.TextField()
    name = models.TextField()
    description = models.TextField()
    geo_loc_original = models.TextField()
    manufacturer = models.TextField()
