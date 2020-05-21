from django.contrib import admin
from .models import Manufacturers, GeoIndication
from django import forms

import pickle
import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from pymystem3 import Mystem

russian_stopwords = stopwords.words("russian")
mystem = Mystem()

E_RE = re.compile(r'ё')
PUNCTUATION_RE = re.compile(r'[!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~]')
GOOD_SYMBOLS_RE = re.compile(r'[^a-za-я\- ]')
DUPLICATE_SPACES_RE = re.compile(r'\s+')


def prepare_text(text):
    text = text.lower()

    text = E_RE.sub('е', text)
    text = PUNCTUATION_RE.sub(' ', text)
    text = GOOD_SYMBOLS_RE.sub('', text)

    text = ' '.join(mystem.lemmatize(text))

    text = ' '.join([token for token in text.split(' ') if token not in russian_stopwords])

    text = DUPLICATE_SPACES_RE.sub(' ', text).strip(' ')
    return text


def load_model(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


class TypeForm(forms.ModelForm):
    def defineType(self):
        # do something that validates your data
        return 'Разное'


class ManufacturersAdmin(admin.ModelAdmin):
    model = Manufacturers
    list_display = ['id', 'mainId', 'manufacturer', 'description', 'status', 'href']


class GeoIndicationAdmin(admin.ModelAdmin):
    model = GeoIndication
    list_display = ['id', 'name', 'description', 'status', 'href', 'geo_loc_original', 'target']

    def save_model(self, request, obj, form, change):
        if not obj.target:
            clf = load_model('models/classifier.pkl')
            mlb = load_model('models/multilabel.pkl')
            vectorizer = load_model('models/vectorizer.pkl')

            vect = vectorizer.transform([prepare_text(obj.description)])
            pred = mlb.inverse_transform(clf.predict(vect))

            if vect.count_nonzero() == 0 or len(pred[0]) == 0:
                obj.target = 'Другое'
            else:
                obj.target = pred[0][0]

        super().save_model(request, obj, form, change)


admin.site.register(Manufacturers, ManufacturersAdmin)
admin.site.register(GeoIndication, GeoIndicationAdmin)
