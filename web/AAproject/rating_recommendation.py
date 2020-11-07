# from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds

# import matplotlib.pyplot as plt
# import seaborn as sns
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import csv 
import os
# print(os.getpcd)
df_area=pd.read_csv('./df_area.csv',encoding='utf-8')
df_user=pd.read_csv('./df_user.csv',encoding='utf-8')

# 주석
# score_list: 56개 평점값 입력 [0, 5, 4, 3, ...., 5, 0, 0, 1]


num=df_user.iloc[-1,0]+1

def main(score_list):
    global df_user
    a=pd.DataFrame(score_list)
    
    a=[]
    for i in range(56):
#         a.append(num) # userid
#         a.append(i) # areaid
#         a.append(score_list[i]) # random rating
#         b=pd.DataFrame(columns=["userid","areaid","rating"])
#         b["userid"]=num
#         b["areaid"]=i
#         b["rating"]=score_list[i]
#         print(b)
        new_data = {"userid" : num, "areaid" : i, "rating" : score_list[i]}
        df_user=df_user.append(new_data,ignore_index=True)
#         df_user.iloc[-1]=a
#         df_user=pd.concat([df_user,b],ignore_index=True)
#         print(b)
        a=[]
    
#     print(df_user)
    user_area_data=pd.merge(df_user,df_area,on="areaid")

    user_area_rating = user_area_data.pivot_table(index = 'userid', columns='areaid',values='rating',aggfunc='first').fillna(0)


    # matrix는 pivot_table 값을 numpy matrix로 만든 것 
    matrix = user_area_rating.values
    # user_ratings_mean은 사용자의 평균 평점 
    user_ratings_mean = np.mean(matrix, axis = 1)

    # R_user_mean : 사용자-영화에 대해 사용자 평균 평점을 뺀 것.
    matrix_user_mean = matrix - user_ratings_mean.reshape(-1, 1)


    pd.DataFrame(matrix_user_mean, columns = user_area_rating.columns).head()


    # scipy에서 제공해주는 svd.  
    # U 행렬, sigma 행렬, V 전치 행렬을 반환.

    U, sigma, Vt = svds(matrix_user_mean, k = 12)


    sigma = np.diag(sigma)

    # U, Sigma, Vt의 내적을 수행하면, 다시 원본 행렬로 복원이 된다. 
    # 거기에 + 사용자 평균 rating을 적용한다. 
    svd_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)

    df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns = user_area_rating.columns)


    def recommend_areas(df_svd_preds, user_id, ori_df_area, ori_ratings_df, num_recommendations=5):
        
        #현재는 index로 적용이 되어있으므로 user_id - 1을 해야함.
        user_row_number = user_id - 1 

        # 최종적으로 만든 pred_df에서 사용자 index에 따라 영화 데이터 정렬 -> 영화 평점이 높은 순으로 정렬 됌
        sorted_user_predictions = df_svd_preds.iloc[user_row_number].sort_values(ascending=False)

        # 원본 평점 데이터에서 user id에 해당하는 데이터를 뽑아낸다. 
        user_data = ori_ratings_df[ori_ratings_df.userid == user_id]

        # 위에서 뽑은 user_data와 원본 영화 데이터를 합친다. 
        user_history = user_data.merge(df_area, on = 'areaid').sort_values(['rating'], ascending=False)

        # 원본 영화 데이터에서 사용자가 본 영화 데이터를 제외한 데이터를 추출
        recommendations = ori_df_area[~ori_df_area['areaid'].isin(user_history['areaid'])]

        # 모두 가봤다면 Empty로 에러가발생..
        # # 안본게 없다면 즉,
        if(recommendations.empty==True):# 공백이라면
            recommendations=ori_df_area # 다시 전부 추천

        # 사용자의 영화 평점이 높은 순으로 정렬된 데이터와 위 recommendations을 합친다. 

        recommendations = recommendations.merge( pd.DataFrame(sorted_user_predictions).reset_index(), on = 'areaid')

        # 컬럼 이름 바꾸고 정렬해서 return
        recommendations = recommendations.rename(columns = {user_row_number: 'Predictions'}).sort_values('Predictions', ascending = False).iloc[:num_recommendations, :]

        return user_history, recommendations

    # 여기서 
    already_rated, predictions = recommend_areas(df_svd_preds, num, df_area, df_user, 5)

    print("안녕")
    # print(predictions[])

    return predictions['areaid'].values, predictions['Predictions'].values


# a_list=[]
# for i in range(57):
#     a_list.append(np.random.randint(1,6))


# 메인을 부를때 a_list에 입력 주면 된다.
# result=main(a_list)

# print(ex_df)


