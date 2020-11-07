import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "artproject.settings")
django.setup()

from subapp.models import ArtInfoDB, PerformanceDB, FestivalDB

CSV_PATH ="csv_data/ak_cltur_fstvl_info_202009.csv"
CSV_PATH2="csv_data/ak_progrm_share_ticket_list_202005.csv"
#csv 파일 확정되면 경로 설정()

count = 1
with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        
        ArtInfoDB.objects.create(
            title = row['event_nm'],
            host = row['auspc_instt_nm'],
            region = None,
            category = '축제/행사',
            start_date = row['event_bgn_de'],
            end_date = row['event_end_de'],
        )

        FestivalDB.objects.create(
            artinfo = ArtInfoDB.objects.get(pk = count),
            content = row['event_dc']#상세내용
        )
        count += 1

        if count % 100 == 0:
            print(count)

print(count)
print('FestivalDB update end')

with open(CSV_PATH2, newline='', encoding='UTF8') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        
        ArtInfoDB.objects.create(
            title = row['pblprfr_nm'],
            host = row['adhrnc_nm'],
            region = row['area_lc'],
            category = '공연/전시',
            start_date = row['rgs_de'],
            end_date = row['rgs_de'],
            )

        PerformanceDB.objects.create(
            artinfo = ArtInfoDB.objects.get(pk = count) ,
            cl = row['ty'],
            genre = row['genre_cl'],
            place = row['prfplc_nm'],
            Vrate = row['viewng_grad_dc'],
        )
        count += 1

        if count % 100 == 0:
            print(count)

print(count)
print('PerformanceDB update end')