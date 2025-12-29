import os
import sys
import csv

sys.path.append(os.path.dirname(os.path.dirname(file)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from core.models import Olymps, Orgs, OlympOrgs


with open('./core/olympiad_organizers.csv', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        olympiad = Olymps.objects.filter(
            full_name=row['olympiad_name'].strip()
        ).first()


for item in data:
    flds = item['fields']

    olympiad = Olymps.objects.filter(
        full_name=flds['olympiad_name']
    ).first()

    if not olympiad:
        print('НЕ НАЙДЕНА ОЛИМПИАДА:', flds['olympiad_name'])
        continue

    orgs = None
    if flds.get('orgs_name'):
        pname = flds['orgs_name'].strip()
        orgs = Orgs.objects.filter(name__iexact=pname).first()
        if not orgs:
            print('НЕ НАЙДЕН ОРГАНИЗАТОР:', repr(pname))

    OlympOrgs.objects.create(
        olympiad=olympiad,
        orgs=orgs,
    )

print('OK')