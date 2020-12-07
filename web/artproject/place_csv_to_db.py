import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "artproject.settings")
django.setup()

from secondapp.models import PlaceDB

CSV_PATH ="csv_data/last_info_data.csv"
#csv 파일 확정되면 경로 설정()

count = 0
with open(CSV_PATH, newline='', encoding='UTF8') as csvfile:
    data_reader = csv.DictReader(csvfile, delimiter='|')
    for row in data_reader:
        
        PlaceDB.objects.create(
            title = row['fclty_nm'],
            address = row['area_addr'],
            region = row['ctprvn_nm'],
            image_url = row['url'],
            allsum = int(row['lcls_all_total_co']) + int(row['otsd_all_total_co']) + int(row['tmp_frnr_all_total_co']) ,

            kids_m = int(row['tmp_lcls_10s_belo_male_co']) + int(row['tmp_otsd_10s_belo_male_co']),
            ten_m = int(row['tmp_lcls_10s_male_co']) + int(row['tmp_otsd_10s_male_co']),
            twenty_m = int(row['tmp_lcls_20s_male_co']) + int(row['tmp_otsd_20s_male_co']),
            thirty_m = int(row['tmp_lcls_30s_male_co']) + int(row['tmp_otsd_30s_male_co']),
            forty_m = int(row['tmp_lcls_40s_male_co']) + int(row['tmp_otsd_40s_male_co']),
            fifty_m = int(row['tmp_lcls_50s_male_co']) + int(row['tmp_otsd_50s_male_co']),
            old_m = int(row['tmp_lcls_60s_above_male_co']) + int(row['tmp_otsd_60s_above_male_co']), #남자 60대이상

            kids_w = int(row['tmp_lcls_10s_belo_female_co']) + int(row['tmp_otsd_10s_belo_female_co']), #여자 10대미만
            ten_w = int(row['tmp_lcls_10s_female_co']) + int(row['tmp_otsd_10s_female_co']),
            twenty_w = int(row['tmp_lcls_20s_female_co']) + int(row['tmp_otsd_20s_female_co']),
            thirty_w = int(row['tmp_lcls_30s_female_co']) + int(row['tmp_otsd_30s_female_co']),
            forty_w = int(row['tmp_lcls_40s_female_co']) + int(row['tmp_otsd_40s_female_co']),
            fifty_w = int(row['tmp_lcls_50s_female_co']) + int(row['tmp_otsd_50s_female_co']),
            old_w = int(row['tmp_lcls_60s_above_female_co']) + int(row['tmp_otsd_60s_above_female_co']),#여자 60대이상
        )
        count += 1

        if count % 100 == 0:
            print(count)

print(count)
print('PlaceDB update end')
