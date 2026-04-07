# 공분산 / 상관계수
# 변수가 하나인 경우에는 분산은 거리와 관련이 있다
# 변수가 두 개인 경우에는 분산은 방향을 가진다

import numpy as np

# 공분산
print(np.cov(np.arange(1, 6), np.arange(2,7)))
print(np.cov(np.arange(1, 6), (3,3,3,3,3)))
print(np.cov(np.arange(1, 6), np.arange(6, 1, -1)))
