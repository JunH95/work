# 어느 음식점의 매출 데이터와 기상청이 제공한 날씨 데이터를 활용하여
# 최고온도에 따른 매출액의 평균에 차이가 있는지 검정
# 세 집단 : 추움, 보통, 더움

# 귀무 : 어느 음식점의 매출 데이터는 온도에 따라 매출액 평균에 차이가 없다.
# 대립 : 어느 음식점의 매출 데이터는 온도에 따라 매출액 평균에 차이가 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

pd.set_option("display.max_columns", None)

# 매출 데이터 읽기
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tsales.csv",  
                        dtype={'YMD':'object'})  # int -> object 변환해 읽기
print(sales_data.head(2))
#         YMD    AMT  CNT
# 0  20190514      0    1
# 1  20190519  18000    1
print(sales_data.info())

# 날씨 데이터 읽기
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tweather.csv")
print(wt_data.head(2))  # 328 * 3
#    stnId          tm  avgTa  minTa  maxTa  sumRn  maxWs  avgWs  ddMes
# 0    108  2018-06-01   23.8   17.5   30.2    0.0    4.3    1.9    0.0
# 1    108  2018-06-02   23.4   17.6   30.1    0.0    4.5    2.0    0.0
print(wt_data.info())   # 702 * 9

print()
# sales: YMD 20190514, wt: tm 2018-06-01 병합을 위해 데이터 변환 필요
wt_data.tm = wt_data.tm.map(lambda x:x.replace("-",""))
print(wt_data.head(2))
#    stnId        tm  avgTa  minTa  maxTa  sumRn  maxWs  avgWs  ddMes
# 0    108  20180601   23.8   17.5   30.2    0.0    4.3    1.9    0.0
# 1    108  20180602   23.4   17.6   30.1    0.0    4.5    2.0    0.0
print()
# 두 데이터를 병합
frame = sales_data.merge(wt_data, how="left", left_on="YMD", right_on='tm')
print(frame.columns) 
# ['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn','maxWs', 'avgWs', 'ddMes']
print(frame.head(), " ", len(frame))  # 328

data = frame.iloc[:, [0,1,7,8]]  # 'YMD', 'AMT','maxTa', 'sumRn' 
print(data.head())
print("결측치 확인 : ", data.isnull().sum())

print(data.maxTa.describe())
# plt.boxplot(data.maxTa)
# plt.show()

# 온도를 세 그룹으로 분리 (int -> 범주형)
print(data.isnull().sum())
data["ta_gubun"] = pd.cut(data.maxTa, bins=[-5, 8, 24, 37], labels=[0, 1, 2])
print(data.head(3), " ", data["ta_gubun"].unique())


# 정규성, 등분산성
x1 = np.array(data[data.ta_gubun == 0].AMT)  # 추움
x2 = np.array(data[data.ta_gubun == 1].AMT)  # 보통
x3 = np.array(data[data.ta_gubun == 2].AMT)  # 더움

print(x1[:5])
print(stats.levene(x1, x2, x3).pvalue)  #  0.03900239 만족 x
print(stats.bartlett(x1, x2, x3).pvalue) # 0.0096775
print()
print(stats.shapiro(x1).pvalue)  # 0.24819
print(stats.shapiro(x2).pvalue)  # 0.03882
print(stats.shapiro(x3).pvalue)  # 0.31829
print()

# 온도별 매출액 평균
np.set_printoptions(suppress=True, precision=10)
spp = data.loc[:, ["AMT", "ta_gubun"]]
print(spp.groupby("ta_gubun").mean())
print(np.mean(x1))  # 1032362.318840
print(np.mean(x2))  # 818106.870
print(np.mean(x3))  # 553710.93

group1 = x1
group2 = x2
group3 = x3

print(stats.f_oneway(group1, group2, group3))
# statistic=99.1908012029983, pvalue=2.360737101089604e-34
# 해석 pvalue = 2.360737101089604e-34 < 0.05 이므로 귀무가설 기각
# 어느 음식점의 매출 데이터는 온도에 따라 매출액 평균에 차이가 있다.

# 정규성 깨지면 stats.kruskal() 사용, 등분산이 깨지면 welch's ANOVA

print(stats.kruskal(group1,group2,group3))
# KruskalResult(statistic=132.7022591443371, pvalue=1.5278142583114522e-29) 귀무 가설 기각

# pip install pingouin
from pingouin import welch_anova
print(welch_anova(dv="AMT", between="ta_gubun", data=data))
#      Source  ddof1     ddof2           F         p_unc       np2
# 0  ta_gubun      2  189.6514  122.221242  7.907874e-35  0.379038
# 귀무가설 기각

print()
# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=spp['AMT'], groups=spp['ta_gubun'], alpha=0.05)
print(tukResult)

# 시각화
tukResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()