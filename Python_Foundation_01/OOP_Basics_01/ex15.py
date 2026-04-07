# pack1/ex15 - main
print("사용자 정의 모듈 처리하기")
s = 20      # 뭔가를 하다가..모듈이 필요한 경우
print("\n경로 지정 방법1 : import 모듈명")
import pack1.mymod1
print(dir(pack1.mymod1))
print(pack1.mymod1.__file__)
print(pack1.mymod1.__name__)
list1 = [1, 2]
list2 = [3, 4, 5]
pack1.mymod1.listHap(list1, list2)

if __name__ == "__main__": print("나는 메인모듈~~~")

print("\n경로 지정 방법2 : from 모듈명 import 함수명(메소드명 포함) 또는 변수명")
from pack1.mymod1 import kbs
kbs()
from pack1.mymod1 import kbs, mbc, tot
mbc()
print(tot)

from pack1.mymod1 import *    # *을 사용해 pack1.mymod1 모듈의 모든 멤버 로딩 (비권장)
print("tot :", tot)

from pack1.mymod1 import kbs as k     # kbs의 별명을 k 로 사용

print("\n경로 지정 방법3 : import 하위패키지.모듈명")
import pack1.subpack.sbs
pack1.subpack.sbs.sbsMansae()
import pack1.subpack.sbs as nickname
nickname.sbsMansae()

print("\n경로 지정 방법4 : 현재 package와 동등한 다른 패키지 모듈 읽기")
# import ../pack1_other.mymod2
from pack1_other import mymod2
mymod2.hapFunc(4, 3)

# 터미널에서 pro1으로 나와서 python -m pack1.ex15 명령어 대신 그전에 사용했던 하위 모듈 앞에 pack1. 이 붙어야 한다

import mymod3
result = mymod3.gopFunc(4, 3)
print("path가 설정된 곳의 module 읽기 - result:", result)
# 가상환경에서 설정된 곳에 Lib 폴더 안에 모듈을 넣으면 바로 import 할 수 있다

print("end")
    