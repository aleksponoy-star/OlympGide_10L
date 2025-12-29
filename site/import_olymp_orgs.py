import os
import sys
import csv

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from core.models import Olymps, Orgs, OlympOrgs


with open('./core/olympiad_organizers.csv', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        olymp_name = row['olympiad_name'].strip()
        org_name = row['organizer_name'].strip()

        olympiad = Olymps.objects.filter(full_name=olymp_name).first()
        if not olympiad:
            print('НЕ НАЙДЕНА ОЛИМПИАДА:', olymp_name)
            continue

        orgs = Orgs.objects.filter(name__iexact=org_name).first()
        if not orgs:
            print('НЕ НАЙДЕН ОРГАНИЗАТОР:', org_name)
            continue

        OlympOrgs.objects.get_or_create(
            olympiad=olympiad,
            orgs=orgs,
        )

print('OK')
