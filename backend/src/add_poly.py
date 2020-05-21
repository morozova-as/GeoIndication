import sys, os
from define_geo_by_id import defineFromText


def append_geo(id_object):
    df = GeoIndication.objects.get(id=id_object)
    print('Установка полигона для следующего наименования:')
    print(df.name)
    print('Верно? (1 - да, 0 - нет)')

    answer = int(input())

    if answer:
        defined_polygon = defineFromText(df.geo_loc_original)
        if defined_polygon:
            df.geo_loc_polygon = defined_polygon
            df.save()
            return id_object
        return None
    else:
        print('Перезапустите скрипт с исправленными параметрами')
        return None


if __name__ == '__main__':

    pr_dir = os.path.abspath('geo_indication')
    sys.path.append(pr_dir)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

    import django

    django.setup()

    from map.models import GeoIndication

    try:
        id_to_change = sys.argv[1]

        result = append_geo(id_to_change)
        if not result:
            raise ValueError
        else:
            print('Для наименования с id =', id_to_change, 'задан объект, описывающий геополигон')
    except ValueError:
        print('Произошла ошибка. Неверно указаны параметры или в тексте не найдены географические объекты')
