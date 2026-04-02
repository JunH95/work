import numpy as np
from scipy import stats

blue = np.array([70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80])
red = np.array([60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66])

# 귀무 : 포장지 색상에 따른 제품의 매출액에 차이가 없다.
# 대립 : 포장지 색상에 따른 제품의 매출액에 차이가 있다.

shapiro_blue = stats.shapiro(blue)
shapiro_red = stats.shapiro(red)
print(shapiro_blue)
print(shapiro_red)
# p > 0.05 정규성 만족


levene = stats.levene(blue, red)
print(f"Levene p-value: {levene.pvalue:.4f}")
# p 0.4392 > 0.05 등분산성 만족


t_stat, p_val = stats.ttest_ind(blue, red, equal_var=True)

print(f"t-통계량: {t_stat:.4f}")
print(f"p-value: {p_val:.4f}")

# 결론: p-value 0.0083 < 0.05 이므로 귀무가설을 기각
# 포장지 색상에 따른 매출액에 통계적으로 유의미한 차이가 존재


import numpy as np
from scipy import stats

men_pop = np.array([0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8])
women_pop = np.array([1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4])

men_sample = np.random.choice(men_pop, 15, replace=False)
women_sample = np.random.choice(women_pop, 15, replace=False)


# 귀무 : 남녀 간 콜레스테롤 양에 차이가 없다.
# 대립 : 남녀 간 콜레스테롤 양에 차이가 있다.

shapiro_men = stats.shapiro(men_sample)
shapiro_women = stats.shapiro(women_sample)
print("--- 2. 정규성 검정 결과 ---")
print(f"남자 p-value: {shapiro_men.pvalue:.4f}")
print(f"여자 p-value: {shapiro_women.pvalue:.4f}")

if shapiro_men.pvalue > 0.05 and shapiro_women.pvalue > 0.05:
    # 등분산성 확인
    levene = stats.levene(men_sample, women_sample)
    is_equal = levene.pvalue > 0.05
    t_stat, p_val = stats.ttest_ind(men_sample, women_sample, equal_var=is_equal)
    test_name = "독립표본 t-검정"

else:
    # Mann-Whitney U 검정 수행
    u_stat, p_val = stats.mannwhitneyu(men_sample, women_sample, alternative='two-sided')
    test_name = "Mann-Whitney U 검정"


print(f"분석 방법: {test_name}")
print(f"p-value: {p_val:.4f}")

alpha = 0.05
if p_val < alpha:
    print("\n결론: p-value가 0.05보다 작으므로 귀무가설을 기각")
    print("남녀 간 콜레스테롤 양에 통계적으로 유의미한 차이가 존재")
else:
    print("\n결론: p-value가 0.05보다 크므로 귀무가설을 채택")
    print("남녀 간 콜레스테롤 양에 통계적으로 유의미한 차이가 있다고 볼 수 없음.")

import pandas as pd
import numpy as np
from scipy import stats
import MySQLdb

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123', db='test', charset='utf8')
    sql = """
        SELECT b.busername, j.jikwonpay 
        FROM jikwon j 
        JOIN buser b ON j.busernum = b.buserno 
        WHERE b.busername IN ('총무부', '영업부')
    """
    df = pd.read_sql(sql, conn)
except Exception as e:
    pass
finally:
    conn.close()

# 결측치 처리 
df['jikwonpay'] = df['jikwonpay'].fillna(
    df.groupby('busername')['jikwonpay'].transform('mean')
)

# 데이터 분리
total_dept = df[df['busername'] == '총무부']['jikwonpay']
sales_dept = df[df['busername'] == '영업부']['jikwonpay']


# 귀무 : 총무부와 영업부 직원의 연봉 평균에 차이가 없다.
# 대립 : 총무부와 영업부 직원의 연봉 평균에 차이가 있다.

# 정규성 검정
shapiro_total = stats.shapiro(total_dept)
shapiro_sales = stats.shapiro(sales_dept)
print(f"총무부 p-value: {shapiro_total.pvalue:.4f}")
print(f"영업부 p-value: {shapiro_sales.pvalue:.4f}")
# p < 0.05 정규성 만족 안함

u_stat, p_val = stats.mannwhitneyu(total_dept, sales_dept, alternative='two-sided')
print(f"p-value: {p_val:.4f}")
# 결론: p-value 0.4721 가 0.05보다 크므로 귀무가설을 채택
# 총무부와 영업부 간의 연봉 평균에 통계적으로 유의미한 차이가 있다고 볼 수 없음.

import numpy as np
from scipy import stats

midterm = np.array([80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80])
final = np.array([90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95])

# 귀무 : 중간고사와 기말고사 성적의 차이가 없다.
# 대립 : 중간고사와 기말고사 성적의 차이가 있다.


# 정규성 검정
diff = final - midterm
shapiro_test = stats.shapiro(diff)

print(f"차이값의 정규성 검정 p-value: {shapiro_test.pvalue:.4f}")
# p 0.3011 > 0.05 정규성 만족

t_stat, p_val = stats.ttest_rel(midterm, final)

print(f"t-통계량: {t_stat:.4f}")
print(f"p-value: {p_val:.4f}")


# 결론: p-value가 {alpha}보다 작으므로 귀무가설을 기각
# 즉, 이 학급의 중간고사와 기말고사 성적 사이에는 유의미한 차이가 있으며 
# 학업능력이 변화했다고 볼 수 있음