from geo_indication.urls import path
from . import views

urlpatterns = [

    path('get_indications_names/', views.get_indications_names),
    path('get_indications_classes/', views.get_indications_classes),
    path('get_polygons_by_facets/', views.get_polygons_by_facets),
    path('get_ids_product/', views.get_ids_product),
    path('get_info/', views.get_info),
    path('get_image_for_product/', views.get_image_for_product),
    path('check_polygons/', views.check_polygons),
    path('define_geo_polygon/', views.define_geo_polygon)

]
