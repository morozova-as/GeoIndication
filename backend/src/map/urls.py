from geo_indication.urls import path
from . import views

urlpatterns = [
    path('update_place/', views.update_place),
    path('get_goods/', views.get_goods),
    path('get_place/', views.get_place),
    path('get_info/', views.get_info),
    path('get_all_names/', views.get_all_names),
    path('get_the_same/', views.get_the_same)

]
