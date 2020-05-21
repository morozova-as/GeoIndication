from django.http import HttpResponse, JsonResponse, FileResponse
from django.http.request import HttpRequest
from map.models import Manufacturers, GeoIndication
from django.core import serializers
from django.middleware.csrf import get_token
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from os import path

from django.views.decorators.csrf import csrf_exempt
import json


# from .utils import find_locs

def create_csrf_token(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'csrfToken': get_token(request)})


# def update_place(request):
#     s = serializers.serialize('json', Place.objects.all())
#     return HttpResponse(s, content_type='json')
#
#
# def get_info(request):
#     name = request.POST['name'].upper()
#     good_place = Goods.objects.filter(name=name)
#     print(name)
#     print(good_place)
#     s = serializers.serialize('json', good_place)
#     return HttpResponse(s, content_type='json')
#
#
# def get_the_same(request):
#     set_places = set()
#     arr = []
#     name = request.POST['name'].upper()
#     good_place = Goods.objects.filter(name=name)
#     for i in good_place:
#         set_places.add(i.new_place)
#
#     print(set_places)
#     for i in set_places:
#         other_name = Goods.objects.filter(new_place=i)
#         arr.append(other_name)
#
#     print(arr)
#     for i in range(len(arr) - 1):
#         arr[i + 1] = arr[i].union(arr[i + 1])
#
#     s = serializers.serialize('json', arr[len(arr) - 1])
#     return HttpResponse(s, content_type='json')
#
#
# def get_place(request):
#     set_places = set()
#     arr = []
#     name = request.POST['name'].upper()
#     good_place = Goods.objects.filter(name=name)
#
#     for i in good_place:
#         set_places.add(i.new_place)
#
#     for i in set_places:
#         coord_place = Place.objects.filter(name=i)
#         arr.append(coord_place)
#     for i in range(len(arr) - 1):
#         arr[i + 1] = arr[i].union(arr[i + 1])
#     s = serializers.serialize('json', arr[len(arr) - 1])
#
#     return HttpResponse(s)
#
#
# def get_all_names(request):
#     to_find = []
#     for i in range(len(request.POST) - 1):
#         to_find.append(request.POST["type_" + str(i)])
#     arr = []
#
#     for i in range(len(to_find)):
#         good_place = Goods.objects.filter(specification__contains=to_find[i])
#         arr.append(good_place)
#
#     for i in range(len(arr) - 1):
#         arr[i + 1] = arr[i].union(arr[i + 1])
#     s = serializers.serialize('json', arr[len(arr) - 1])
#
#     return HttpResponse(s, content_type='json')


@csrf_exempt
def get_goods(request):
    s = serializers.serialize('json', GeoIndication.objects.all())

    return HttpResponse(s, content_type='json')


@csrf_exempt
def get_indications_names(request):
    names = list(GeoIndication.objects.values_list('name', flat=True))
    return JsonResponse(names, safe=False)


@csrf_exempt
def get_indications_classes(request):
    classes = list(GeoIndication.objects.values_list('target', flat=True))
    classes_uniq = list(set(classes))
    return JsonResponse(classes_uniq, safe=False)


@csrf_exempt
def get_polygons_by_facets(request):
    data = json.loads(request.body)
    names = data['names']
    types = data['types']

    query = GeoIndication.objects.all()
    if names:
        query = query.filter(name__in=names)
    if types:
        query = query.filter(target__in=types)

    query = query.values_list('geo_loc_polygon', 'id')

    respond = list(query)

    if names or types:
        return JsonResponse(respond, safe=False)

    return JsonResponse('', safe=False)


@csrf_exempt
def get_ids_product(request):
    data = json.loads(request.body)
    names = data['names']
    types = data['types']

    query = GeoIndication.objects.all()
    if names:
        query = query.filter(name__in=names)
    if types:
        query = query.filter(target__in=types)

    query = query.values_list('id', flat=True)

    respond = list(query)

    if names or types:
        return JsonResponse(respond, safe=False)

    return JsonResponse('', safe=False)


@csrf_exempt
def get_info(request):
    idMain = json.loads(request.body)
    query = Manufacturers.objects.filter(mainId__in=idMain)
    geo = GeoIndication.objects.all()
    # geo_main = geo.values_list('id', 'geo_loc_original')
    # print(geo_main)
    query = list(query.values_list('description',
                                   'href',
                                   'mainId',
                                   'manufacturer',
                                   'status'))

    dict_query = {}

    for i in range(len(query)):
        q = query[i]
        if q[2] not in dict_query:
            dict_query[q[2]] = []

        geo_main = geo.filter(id=q[2])
        dict_query[q[2]].append({
            "description": q[0],
            "href": q[1],
            "mainId": q[2],
            "manufacturer": q[3],
            "name": geo_main.values_list('name')[0],
            "status": q[4],
            "main_geo_text": geo_main.values_list('geo_loc_original')[0],
            "main_href": geo_main.values_list('href')[0],
            "main_description": geo_main.values_list('description')[0]
        })

    for idOne in idMain:
        numId = int(idOne)
        if numId not in dict_query:
            name = geo.filter(id=numId).values_list('name', 'id', 'geo_loc_original', 'href', 'description')[0]
            dict_query[numId] = [{
                "name": name[0],
                "mainId": name[1],
                "main_geo_text": name[2],
                "main_href": name[3],
                "main_description": name[4],
            }]

    return JsonResponse(dict_query, safe=False)


@csrf_exempt
def get_image_for_product(request):
    key = json.loads(request.body)

    print(key)

    for ext in ['.png', '.jpg', '.jpeg']:
        pathImage = f'media/imgs/{key}{ext}'
        if path.exists(pathImage):
            return FileResponse(open(pathImage, 'rb'))

    return FileResponse(open(f'media/imgs/placeholder.jpg', 'rb'))


def is_point_in_poly(point, poly):
    for i in range(len(poly)):
        arrPoints = []
        for j in range(len(poly[i])):
            arrPoints.append((poly[i][j]['lat'], poly[i][j]['lng']))

        polygon = Polygon(arrPoints)

        if polygon.contains(point):
            return True

    return False


def is_point_in_object(lat, lng, poly):
    polyDict = eval(poly)
    keys = polyDict.keys()
    point = Point(lat, lng)

    for key in keys:
        if is_point_in_poly(point, polyDict[key]['poly']):
            return True

    return False


@csrf_exempt
def check_polygons(request):
    data = json.loads(request.body)

    lat = data['lat']
    lng = data['lng']

    resultNames = []

    geo = GeoIndication.objects.values_list('name', 'geo_loc_polygon')

    for i in range(len(geo)):
        if is_point_in_object(lat, lng, geo[i][1]):
            resultNames.append(geo[i][0])

    return JsonResponse(resultNames, safe=False)


@csrf_exempt
def define_geo_polygon(request):
    #     text_area = json.loads(request.body)
    #
    #     bert = find_locs(text_area)
    #
    #     print(bert)
    #
    return JsonResponse('', safe=False)

#
# import csv
#
# from django.http import HttpResponse
#
#
# def update_place(request):
#     # The only line to customize
#     model_class = Goods
#
#     meta = model_class._meta
#     field_names = [field.name for field in meta.fields]
#
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
#     writer = csv.writer(response)
#
#     writer.writerow(field_names)
#     for obj in model_class.objects.all():
#         row = writer.writerow([getattr(obj, field) for field in field_names])
#
#     return response
