# 이원분산분석 : 요인 복수 - 각 요인의 레벨(그룹)도 복수
# 두 개의 요인에 대한 집단(독립변수) 각각이 종속변수(평균)에 영향을 주는지 검정
# 주효과 : 독립변수들이 각각 독립적으로 종속변수에 미치는 영향을 검정하는 것
# 상호작용효과(교호작용) : 독립변수들이 서로 연관되어 종속변수에 미치는 영향을 검정
# 한 독립변수가 종속변수에 미치는 영향이 다른 독립변수의 수준에 따라 달라지는 현상

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib
from statsmodels.formula.api import 
from statsmodels.stats.anova import anova_lm

# 실습 1 : 태아 수와 관측자 수가 태아의 머리둘레 평균에 영향을 주는가?
# 주효과 가설
# 귀무 : 태아 수와 태아의 머리둘레 평균은 차이가 없다
# 대립 : 태아 수와 태아의 머리둘레 평균은 차이가 있다
# 교호작용 가설
# 귀무 : 교호작용이 없다(태아수와 관측자 수는 관련이 없다)
# 대립 : 교호작용이 있다(태아수와 관측자 수는 관련이 있다)

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3_2.txt")
print(data.head(), data.shape)
print(data["태아수"].unique())
print(data["관측자수"].unique())

# 시각화
# data.boxplot(column="머리둘레", by="태아수")
# plt.show()
# data.boxplot(column="머리둘레", by="관측자수")
# plt.show()