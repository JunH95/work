# 외국인(미국,중국,일본) 국내 관광지(5개) 방문 관광자료 사용
# 나라별 관광지 상관관계 확인하기

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 산점도 그리기
def setScatterGraph():
    pass

def processFunc():
    # 서울시 관광지 정보 파일 
    fname = "서울특별시_관광지입장정보_2011_2016.json"
    jsonTP = json.loads(open(fname, "r", encoding="utf-8").read())
    tour_table = pd.DataFrame(jsonTP, columns=("yyyymm", "resNm", "ForNum"))
    tour_table = tour_table.set_index("yyyymm")
    # print(tour_table)
    resNm = tour_table.resNm.unique()
    # print(resNm[:5])  # ['창덕궁' '운현궁' '경복궁' '창경궁' '종묘']

    # 중국인 관광지 정보 파일 dataframe에 저장
    cdfname = "중국인방문객.json"
    jdata = json.loads(open(cdfname, "r", encoding="utf-8").read())
    china_table = pd.DataFrame(jdata, columns=("yyyymm", "visit_cnt"))
    china_table = china_table.rename(columns={"visit_cnt" : "china"})
    china_table = china_table.set_index("yyyymm")
    print(china_table[:2])

    # 일본인 관광지 정보 파일 dataframe에 저장
    jdfname = "일본인방문객.json"
    jdata = json.loads(open(jdfname, "r", encoding="utf-8").read())
    japan_table = pd.DataFrame(jdata, columns=("yyyymm", "visit_cnt"))
    japan_table = japan_table.rename(columns={"visit_cnt" : "japan"})
    japan_table = japan_table.set_index("yyyymm")
    print(japan_table[:2])

    # 미국인 관광지 정보 파일 dataframe에 저장
    udfname = "미국인방문객.json"
    jdata = json.loads(open(udfname, "r", encoding="utf-8").read())
    usa_table = pd.DataFrame(jdata, columns=("yyyymm", "visit_cnt"))
    usa_table = usa_table.rename(columns={"visit_cnt" : "usa"})
    usa_table = usa_table.set_index("yyyymm")
    print(usa_table[:2])

    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index=True)
    print(all_table)

    r_list = []
    for tourpoint in resNm[:5]:
        r_list.append(setScatterGraph(tour_table, all_table, tourpoint))

if __name__=="__main__":
    processFunc()