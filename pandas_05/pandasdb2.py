# 원격 DB 연동 jikwon 자료를 읽어 dataframe 에 저장
# import MySQLdb
import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import koreanize_matplotlib

config = {
    "host":"127.0.0.1",
    "user":"root",
    "password":"123",
    "database":"test",
    "port":3306,
    "charset":"utf8"
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwonno,jikwonname,busername,jikwonjik,jikwongen,jikwonpay
        from jikwon inner join buser on jikwon.busernum=buser.buserno
    """
    cursor.execute(sql)

    # for (jikwonno,jikwonname,busername,jikwonjik,jikwongen,jikwonpay) in cursor:
    #     print(jikwonno,jikwonname,busername,jikwonjik,jikwongen,jikwonpay)
    df1 = pd.DataFrame(cursor.fetchall(),
                    columns=["jikwonno","jikwonname","busername","jikwonjik","jikwongen","jikwonpay"])
    print(df1.head())
    print("연봉의 총합 : ", df1["jikwonpay"].sum())
    
except Exception as e:
    print("처리 오류 :", e)
finally:
    cursor.close()
    conn.close()
