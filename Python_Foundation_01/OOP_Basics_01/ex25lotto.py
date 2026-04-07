# 클래스 포함 관계 연습 - 로또 
import random

class LottoBall:
    def __init__(self, num):
        self.num = num
        
class LottoMachine:
    def __init__(self):
        self.balllist = []
        for i in range(1, 46):
            self.balllist.append(LottoBall(i))      # 클래스의 포함 관계

    def selectBalls(self):
        # for a in range(45):                   # 리스트에 잘 담겨있는지 확인 차 프린트
        #     print(self.balllist[a].num, end=" ")
        # print(" ")
        random.shuffle(self.balllist)       # 리스트에 담긴 번호 섞기
        # for a in range(45):               # 번호 섞고 잘 섞였는지 확인 차 프린트
        #     print(self.balllist[a].num, end=" ")
        return self.balllist[0:6]
        
class LottoUI:
    def __init__(self):
        self.machine = LottoMachine()     # 포함관계

    def playLotto(self):
        input("로또를 시작하려면 엔터키를 누르세요")
        selectedBalls = self.machine.selectBalls()
        for ball in selectedBalls:
            print("%d"%(ball.num))

if __name__ == "__main__":
#     machine = LottoMachine()
#     print(machine.selectBalls())

    # lot = LottoUI()       # 객체 변수 
    # lot.playLotto()
    LottoUI().playLotto()   # 실행 결과는 위와 같음 