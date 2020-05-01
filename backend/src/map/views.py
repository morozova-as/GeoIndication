from django.http import HttpResponse
from map.models import Place
from map.models import Goods
from django.core import serializers


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


def get_goods(request):
    s = serializers.serialize('json', Goods.objects.all())
    return HttpResponse(s, content_type='json')


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
