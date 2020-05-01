from django.contrib import admin
from .models import Place, Goods


class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ['num', 'name']

class GoodsAdmin(admin.ModelAdmin):
    model = Goods
    list_display = ['num', 'name', 'origin_place', 'new_place', 'img', 'image_img']
    readonly_fields = ['image_img', ]


admin.site.register(Place, PlaceAdmin)


admin.site.register(Goods, GoodsAdmin)
