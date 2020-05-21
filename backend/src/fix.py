import sys, os

pr_dir = '/home/egor/Documents/Nastya/project/backend/src/geo_indication'

sys.path.append(pr_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from map.models import GeoIndication

df = GeoIndication.objects.get(id=130)
print(df.name)
# print(df.geo_loc_polygon)
df.save()