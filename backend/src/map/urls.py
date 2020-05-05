from geo_indication.urls import path
from . import views

urlpatterns = [
    path('update_place/', views.update_place),
    path('get_goods/', views.get_goods),
    path('csrf/', views.create_csrf_token),
    path('get_place/', views.get_place),
    path('get_info/', views.get_info),
    path('get_all_names/', views.get_all_names),
    path('get_the_same/', views.get_the_same),


    path('get_indications_names/', views.get_indications_names),
    path('get_indications_classes/', views.get_indications_classes),
    path('get_polygons_by_facets/', views.get_polygons_by_facets)

]
