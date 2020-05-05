from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from map.models import Place, Goods, Manufacturers, GeoIndication
from django.core import serializers
from django.middleware.csrf import get_token

from django.views.decorators.csrf import csrf_exempt
import json

def create_csrf_token(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'csrfToken': get_token(request)})


def update_place(request):
    s = serializers.serialize('json', Place.objects.all())
    return HttpResponse(s, content_type='json')


def get_info(request):
    name = request.POST['name'].upper()
    good_place = Goods.objects.filter(name=name)
    print(name)
    print(good_place)
    s = serializers.serialize('json', good_place)
    return HttpResponse(s, content_type='json')


def get_the_same(request):
    set_places = set()
    arr = []
    name = request.POST['name'].upper()
    good_place = Goods.objects.filter(name=name)
    for i in good_place:
        set_places.add(i.new_place)

    print(set_places)
    for i in set_places:
        other_name = Goods.objects.filter(new_place=i)
        arr.append(other_name)

    print(arr)
    for i in range(len(arr) - 1):
        arr[i + 1] = arr[i].union(arr[i + 1])

    s = serializers.serialize('json', arr[len(arr) - 1])
    return HttpResponse(s, content_type='json')


def get_place(request):
    set_places = set()
    arr = []
    name = request.POST['name'].upper()
    good_place = Goods.objects.filter(name=name)

    for i in good_place:
        set_places.add(i.new_place)

    for i in set_places:
        coord_place = Place.objects.filter(name=i)
        arr.append(coord_place)
    for i in range(len(arr) - 1):
        arr[i + 1] = arr[i].union(arr[i + 1])
    s = serializers.serialize('json', arr[len(arr) - 1])

    return HttpResponse(s)


def get_all_names(request):
    to_find = []
    for i in range(len(request.POST) - 1):
        to_find.append(request.POST["type_" + str(i)])
    arr = []

    for i in range(len(to_find)):
        good_place = Goods.objects.filter(specification__contains=to_find[i])
        arr.append(good_place)

    for i in range(len(arr) - 1):
        arr[i + 1] = arr[i].union(arr[i + 1])
    s = serializers.serialize('json', arr[len(arr) - 1])

    return HttpResponse(s, content_type='json')



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

    query = query.values_list('geo_loc_polygon')

    respond = list(query)

    if names or types:
        return JsonResponse(respond, safe=False)

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
