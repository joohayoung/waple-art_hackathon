import csv

CSV_PATH ="C:/Users/26162/TeamProject/Aloha/Artthon/art-hackathon/web/artproject/csv_data/last_info_data.csv"
#csv 파일 확정되면 경로 설정()

count = 0
with open(CSV_PATH, newline='', encoding='UTF8') as csvfile:
    data_reader = csv.DictReader(csvfile, delimiter='|')
    for row in data_reader:
        print(row)
        break
        # count += 1
        # if count == 10:
        #     break

print(count)
print('===end===')