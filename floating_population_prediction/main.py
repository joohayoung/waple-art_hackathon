from load_data import load_data, day2month
from arima import make_arima, pred_data
import os

#67 68 71 사용

# 입력받아야 할 부분
c = "" # c에 ex) 현지인 / 외지인 / 외국인 
h = "" # h에 ex) 10대미만 / 10대 / 20대 / 30대 / 40대 / 50대 / 60대이상 / 모두
g = "" # g에 ex) 남자 / 여자
place = "" # 장소 입력받기
fname = "" # 파일경로 변경 필요 ex) ./ㅁㄴㅇㅁㄴㅇ.csv
ymd = "" # month or day ex) day / month

# 주석
# c = "현지인"
# h = "10대미만"
# g = "남자"
# fname = "C:/Users/gmlrn/Desktop/AI_SCHOOL/art_data/k-means/new_combined.csv"
# place = '봉평콧등작은미술관'
# ymd = "day"

def select_order(ymd):

    if ymd == "day":
        return (2,1,0)
    elif ymd == "month" :
        return (2,1,1)

def main(c, h, g, place, fname, ymd):
        
    age_dict = {
        "10대미만" : "10s_belo_",
        "10대" : "10s_",
        "20대" : "20s_",
        "30대" : "30s_",
        "40대" : "40s_",
        "50대" : "50s_",
        "60대이상" : "60s_above_",
        "모두" : "all_total_",
    }
    local_dict = {
        "현지인" : "lcls_",
        "외지인" : "ostd_",
        "외국인" : "frnr_",
    }
    gender_dict = {
        "남자" : "male_",
        "여자" : "female_",
    }

    # 각 변수 값 변경 default
    val = 'tmp_'+local_dict["현지인"]+age_dict["10대미만"]+gender_dict["남자"]+"co"
    # 현지인 10대미만 남자 선택
    # val = 'tmp_'+local_dict[c]+age_dict[h]+gender_dict[g]+"co"    

    order = select_order(ymd)

    df = load_data(fname, place, val)

    if ymd =="month":
        df = day2month(df,place)

    # df = data, order = (p, d, q) ARIMA 분석에 필요한 각 변수 위에 지정해둠.
    model_fit = make_arima(df,order)

    # model_fit = 모델, steps = 이후 몇개의 값을 예측할 것인지.
    n = 7
    pred_list = pred_data(model_fit, n)

    return pred_list

print(main(c, h, g, place, fname, ymd))
