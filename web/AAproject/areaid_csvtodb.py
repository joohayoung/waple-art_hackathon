import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AAproject.settings")
django.setup()

from firstapp.models import Areainfo

CSV_PATH ="./df_area.csv"
#csv 파일 확정되면 경로 설정()
#poster까지 병합된 파일 기준으로 작성 가져오기

count = 0
with open(CSV_PATH, newline='', encoding='UTF8') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        
        Areainfo.objects.create(
            areaid = row['areaid'],
            title = row['title'],
            genres = row['genres'],
        )
        count += 1

        if count % 100 == 0:
            print(count)

print(count)
print('end')