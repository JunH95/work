

import statsmodels.api as sm
from sklearn.datasets import make_regression
import numpy as np

np.random.seed(12)

# 모델 맛보기
# 방법 1 : make_regression 사용 

x, y, coef = make_regression(n_samples=50, n_features=1, bias=)