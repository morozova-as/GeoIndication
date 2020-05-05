from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe


# class Goods(models.Model):
#     num = models.IntegerField()
#     name = models.CharField(max_length=200)
#     origin_place = models.TextField()
#     specification = models.TextField()
#     rh_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#     actual = models.CharField(max_length=100)
#     url = models.TextField()

# def image_img(self):
#     if self.img:
#         return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img.url)
#     else:
#         return '(Нет изображения)'
#     # image_img.short_description = 'Картинка'
#     # image_img.allow_tags = True


class Place(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField()


class Goods(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=200)
    origin_place = models.TextField()
    new_place = models.TextField()
    rh_name = models.TextField()
    specification = models.TextField()
    rh_address = models.TextField()
    rh_country = models.CharField(max_length=100)
    actual = models.CharField(max_length=100)
    url = models.TextField()
    img = models.ImageField(upload_to='imgs/', null=True,  blank=True)

    def image_img(self):
        if self.img:
            return mark_safe('<img src="%s" width="100"/>' % self.img.url)
        else:
            return '(none)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True


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

# class Manufacturer(models.Model):
#     num = models.IntegerField()
#     name = models.TextField()
#     address = models.TextField(blank=True, null=True)
#     country = models.CharField(blank=True, null=True, max_length=100)
#
#
# class CorrectPlace(models.Model):
#     num = models.IntegerField()
#     origin_place = models.TextField()
#     new_place = models.TextField()
