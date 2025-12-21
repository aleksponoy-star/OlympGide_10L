# core/import_olymp_napr.py
import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from core.models import Olymps, Profil, Predmet, Level, OlympNapr


with open('./core/olymp_napr.json', encoding='utf-8') as f:
    data = json.load(f)


for item in data:
    flds = item['fields']

    olympiad = Olymps.objects.filter(
        full_name=flds['olympiad_name']
    ).first()

    if not olympiad:
        print('НЕ НАЙДЕНА ОЛИМПИАДА:', flds['olympiad_name'])
        continue

    profile = None
    if flds.get('profil_name'):
        pname = flds['profil_name'].strip()
        profile = Profil.objects.filter(name__iexact=pname).first()
        if not profile:
            print('НЕ НАЙДЕН ПРОФИЛЬ:', repr(pname))


    predmet = None
    if flds.get('predmet_name'):
        prname = flds['predmet_name'].strip()
        predmet = Predmet.objects.filter(name__iexact=prname).first()
        if not predmet:
            print('НЕ НАЙДЕН ПРЕДМЕТ:', repr(prname))


    level = None
    if flds.get('level_name'):
        level = Level.objects.filter(name=flds['level_name']).first()
        if not level:
            print('НЕ НАЙДЕН УРОВЕНЬ:', flds['level_name'])

    OlympNapr.objects.create(
        olympiad=olympiad,
        profil=profile,
        predmet=predmet,
        level=level,
    )

print('OK')

