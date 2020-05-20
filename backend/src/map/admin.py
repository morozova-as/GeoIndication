from django.contrib import admin
from .models import Place, Goods, Manufacturers, GeoIndication


# class PlaceAdmin(admin.ModelAdmin):
#     model = Place
#     list_display = ['num', 'name']
#
# class GoodsAdmin(admin.ModelAdmin):
#     model = Goods
#     list_display = ['num', 'name', 'origin_place', 'new_place', 'img', 'image_img']
#     readonly_fields = ['image_img', ]

class ManufacturersAdmin(admin.ModelAdmin):
    model = Manufacturers
    list_display = ['id', 'mainId', 'manufacturer', 'name', 'description', 'status', 'href', 'geo_loc_original']


class GeoIndicationAdmin(admin.ModelAdmin):
    model = GeoIndication
    list_display = ['id', 'name', 'description', 'status', 'href', 'geo_loc_original', 'target', 'geo_loc_polygon']


admin.site.register(Manufacturers, ManufacturersAdmin)
admin.site.register(GeoIndication, GeoIndicationAdmin)
