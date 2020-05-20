from django.contrib import admin
from .models import Manufacturers, GeoIndication

class ManufacturersAdmin(admin.ModelAdmin):
    model = Manufacturers
    list_display = ['id', 'mainId', 'manufacturer', 'name', 'description', 'status', 'href', 'geo_loc_original']


class GeoIndicationAdmin(admin.ModelAdmin):
    model = GeoIndication
    list_display = ['id', 'name', 'description', 'status', 'href', 'geo_loc_original', 'target', 'geo_loc_polygon']


admin.site.register(Manufacturers, ManufacturersAdmin)
admin.site.register(GeoIndication, GeoIndicationAdmin)
