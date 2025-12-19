import csv
import json
MODEL = "core.ofd"
START_PK = 1
data = []
with open(
    "c:/Users/alekspon3/Desktop/проект/ofd.csv",
    encoding="cp1251"
) as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    print("CSV rows:", len(rows))
    pk = START_PK
    for row in rows:
        data.append({
            "model": MODEL,
            "fields": row
        })
    pk += 1
with open("c:/Users/alekspon3/Desktop/проект/ofd.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)




