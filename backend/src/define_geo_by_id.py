from deeppavlov import configs, build_model

ner_model_bert = build_model(configs.ner.ner_rus_bert, download=True)

import requests
import time
import re
import numpy as np

separators = [None, ',', '.', ';']
base_url = 'https://nominatim.openstreetmap.org/search?'
details_url = 'https://nominatim.openstreetmap.org/details.php?'
base_params = dict(
    dedupe='1',
    format='geocodejson',
    polygon='1',
    extratags='1',
    polygon_geojson=1,
    addressdetails=1
)
details_params = dict(
    dedupe='1',
    format='json',
    polygon='1',
    extratags='1',
    polygon_geojson=1,
    addressdetails=1
)

dict_levels = {
    'administrative': [2, 4, 5],
    'peninsula': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'city': [5, 6],
    'town': [5, 6],

    'village': [6, 7, 8],
    'hamlet': [7, 8],
    'isolated_dwelling': [7, 8],
    'locality': [7, 8],
    'allotments': [6, 7, 8],
    'neighbourhood': [6, 7, 8, 9, 10],
    'island': [6, 7, 8, 9, 10],

    'resort': [6, 7, 8, 9, 10],
    'industrial': [6, 7, 8, 9, 10],
    'residential': [6, 7, 8, 9, 10],

    'water': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'bay': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

}

not_replace = ['Брешиа']


def define_locs(bert):
    all_loc = []
    curr_loc = []
    lenght = len(bert[0])
    for i in range(lenght):
        list_items = list(zip(bert[0][i], bert[1][i]))
        for k, v in list_items:
            if (v == 'B-LOC'):
                if (curr_loc):
                    all_loc.append(' '.join(curr_loc))
                    curr_loc = []
                curr_loc.append(k)
            elif (v == 'I-LOC'):
                if (curr_loc):
                    curr_loc.append(k)
            else:
                if (curr_loc):
                    all_loc.append(' '.join(curr_loc))
                    curr_loc = []
        if (curr_loc):
            all_loc.append(' '.join(curr_loc))
            curr_loc = []
    return all_loc


def find_locs(line):
    ind = 0
    flag = True
    res_bert = None

    while flag:
        try:
            sep = separators[ind]
            if sep:
                new_line = line.split(sep)
                res_bert = ner_model_bert(new_line)
            else:
                res_bert = ner_model_bert([line])

            flag = False

        except:
            ind += 1

    if res_bert:
        res_loc = define_locs(res_bert)
        if res_loc:
            return res_loc

    return None


def normalizeGeoLocation(geo):
    time.sleep(1)
    flag = 1

    for i in range(len(geo)):
        new_geo = geo[i].strip()
        new_geo = new_geo.lower()
        new_geo = re.sub(r'(ий|ого|ым) (район|района|районом|р - на|р - н)$', 'ий район', new_geo)
        new_geo = re.sub(r'(ой|ая) (обл|область|области)$', 'ая область', new_geo)
        new_geo = re.sub(r'(ого) (края)$', 'ий край', new_geo)
        new_geo = re.sub(r'(ой) (федерации)$', 'ая федерация', new_geo)
        new_geo = re.sub(r'(ой) (республики)$', 'ая республика', new_geo)
        new_geo = re.sub(r'(ого) (месторождения)$', 'ое месторождение', new_geo)

        geo[i] = new_geo

    while flag:

        print('\n')
        print("Результат после нормализации объектов:")
        for index, value in enumerate(geo):
            print(index, ": ", value)

        print('Если есть элемент, где была допущена ошибка, введите номер (оставте пустым, если все хорошо):')
        num_error = input()
        if (num_error):
            print('Введите новое значение для выбранного элемента:')
            geo[int(num_error)] = input()
        else:
            flag = 0

    print('\n')
    print("Итоговый результат:")
    for index, value in enumerate(geo):
        print(index, value)

    print('\n')
    return geo


def max_level(dict_levels):
    keys = dict_levels.keys()
    return max(list(map(lambda x: int(re.sub('level', '', x)), keys)))


def get_key(val, dict_):
    arr = []
    for key, value in dict_.items():
        if val == value:
            arr.append(key)
    return arr


def get_number_search_items(arr):
    unique, counts = np.unique(arr, return_counts=True)
    dict_ = dict(zip(unique, counts))
    return np.prod(np.array(list(dict_.values()))), dict_


def define_new_search(dict_items):
    new_search = []
    keys, values = list(dict_items.keys()), list(dict_items.values())
    count_items, dict_count_levels = get_number_search_items(values)
    new_search = [{}]

    for level in range(11):
        if level in values:
            count_level = dict_count_levels[level]
            if (count_level == 1):
                for i in range(len(new_search)):
                    new_search[i][level] = get_key(level, dict_items)[0]
            else:
                last_dict = new_search[-1]
                new_search[-1][level] = get_key(level, dict_items)[0]
                for i in range(count_level - 1):
                    new_search.append(last_dict.copy())
                    new_search[-1][level] = get_key(level, dict_items)[i + 1]

    return (new_search)


def fix_levels(dict_levels):
    new_dict = {}
    for key, value in dict_levels.items():
        if ((value[0] == 6 and value[1] == 'administrative' and key not in not_replace) or (
                key.lower().find('район') >= 0) or (key.lower().find('республика') >= 0)):
            new_dict[key] = 5
        elif (value[0] == 7 or value[0] == 8 or value[0] == 9 or value[0] == 10):
            new_dict[key] = 6
        else:
            new_dict[key] = value[0]

    return (new_dict)


def first_stage(geo):
    all_levels = {}
    for cur_place in geo:
        if (cur_place == ' '):
            continue

        params = base_params.copy()
        params['q'] = cur_place
        req = requests.get(url=base_url, params=params)
        find_object = req.json()['features']

        right_object = list(filter(lambda x: x['properties']['geocoding']['type'] in dict_levels.keys() and (
                    x['geometry']['type'] == 'Polygon' or x['geometry']['type'] == 'MultiPolygon'), find_object))

        if not right_object:
            continue

        curr_levels = []

        for one_object in right_object:
            props = one_object['properties']['geocoding']
            geom = one_object['geometry']

            curr_levels.append(max_level(props['admin']))

        all_levels[cur_place] = [max(curr_levels), right_object[0]['properties']['geocoding']['type']]

    return (all_levels)


def find_index(arr):
    for i in range(len(arr)):
        info = arr[i]['properties']['geocoding']
        if info['type'] in dict_levels.keys():
            return i

    return 0


def try_search(search):
    params = base_params.copy()
    params['q'] = search
    req = requests.get(url=base_url, params=params)
    return req.json()['features']


def define_lat_lon(place_id):
    params = details_params.copy()
    params['place_id'] = place_id
    req = requests.get(url=details_url, params=params)
    return req.json()['centroid']['coordinates']


def define_poly(dict_search):
    poly = []
    keys, values = list(dict_search.keys()), list(dict_search.values())
    search = ' '.join(values)

    find_object = try_search(search)
    right_object = list(filter(lambda x: x['properties']['geocoding']['type'] in dict_levels.keys() and (
                x['geometry']['type'] == 'Polygon' or x['geometry']['type'] == 'MultiPolygon'), find_object))

    len_finds = len(right_object)

    if (len_finds > 0):
        index = find_index(right_object)
        info = right_object[index]['properties']['geocoding']
        geo_info = right_object[index]['geometry']

        lon, lat = define_lat_lon(info['place_id'])
        return lon, lat, info['label'], info['place_id'], geo_info['type'], geo_info['coordinates']
    else:
        if (5 in keys):
            del dict_search[5]

            keys, values = list(dict_search.keys()), list(dict_search.values())
            search = ' '.join(values)
            right_object = try_search(search)
            len_finds = len(right_object)
            if (len_finds > 0):
                index = 0
                info = right_object[index]['properties']['geocoding']
                geo_info = right_object[index]['geometry']

                lon, lat = define_lat_lon(info['place_id'])
                return lon, lat, info['label'], info['place_id'], geo_info['type'], geo_info['coordinates']
        else:
            print(dict_search)
            print("NOT FIND")
            return None, None, None, None, None, None

    return None, None, None, None, None, None


def get_poly_for_polygon(poly):
    one_poly = []
    for point in poly:
        one_poly.append({
            'lat': point[1],
            'lng': point[0]
        })
    return one_poly


def fix_poly_view(polys, geo_type):
    new_poly = []
    if (geo_type == 'MultiPolygon'):
        for polygon in polys:
            new_poly.append(get_poly_for_polygon(polygon[0]))
    else:
        new_poly.append(get_poly_for_polygon(polys[0]))

    return new_poly


def define_coords(geo):
    result_poly_dict = {}

    all_levels = first_stage(geo)
    all_levels_fix = fix_levels(all_levels)

    new_search = define_new_search(all_levels_fix)

    arr_label_to_show = []
    for item in new_search:
        lng, lat, label, place_id, geo_type, one_poly = define_poly(item)
        arr_label_to_show.append(label)
        if (one_poly):
            poly = fix_poly_view(one_poly, geo_type)

            result_poly_dict[place_id] = {
                'label': label,
                'centroid': {
                    'lat': lat,
                    'lng': lng
                },
                'poly': poly
            }

    print('\n')
    print('Найдены полигоны для следующих географических объектов:')
    for index, value in enumerate(list(set(arr_label_to_show))):
        print(value)

    print('\n')
    print(
        'Если поиск не дал результатов или они не верны можно повторить его, переформулиров текст или изменив значение после обработки анализатора.')

    return result_poly_dict


def defineFromText(text):
    if not text or len(text) == 0:
        print('Поле с географическим описанием наименование пустое')
        return None

    arrayLocs = find_locs(text)
    if not arrayLocs:
        return None

    print('Результат после работы анализатора текста на определение географических объектов:')
    print(arrayLocs)
    arrayNormLocs = normalizeGeoLocation(arrayLocs)
    polyObject = define_coords(arrayNormLocs)

    print('Обработка закончена')

    return polyObject

