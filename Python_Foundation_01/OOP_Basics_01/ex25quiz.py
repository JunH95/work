# 카페 연습문제 : 클래스 python 카테고리 24번
# 조건
# 입력자료는 키보드를 사용
# 커피는 한 잔에 200원
# 100원 넣고 커피를 요구하면 요금 부족 메시지 출력
# 400원 넣고 2잔 요구하면 두 잔 출력
# 500원 넣고 1잔 요구하면 300원 반납
# 출력 형태 -------------
# 동전을 입력하세요 : 400
# 몇 잔을 원하세요 : 2
# 커피 2잔과 잔돈 0원

# Machine 클래스 cupCount = 1, showData()
# coinIn 클래스 coin, change, culc(cupCount), coinIn은 Machine에 포함

class CoinIn:
    def __init__(self):
        self.coin = 0
        self.change = 0

    def calc(self, coin, cupCount):
        coffee = 200
        total_coffee = coffee * cupCount

        if coin < total_coffee:
            print("요금이 부족합니다.")
        else:
            self.change = coin - total_coffee
            print(f"커피 {cupCount}잔과 잔돈 {self.change}원")
    
class Machine:
    
    def __init__(self):
        self.cupCount = 1
        self.coin_part = CoinIn()
    
    def showData(self):
        coin = int(input("동전을 입력하세요 : "))
        cupcount = int(input("몇 잔을 원하세요 : "))

        self.coin_part.calc(coin, cupcount)

m = Machine()
m.showData()


class CoffeMachine:
    def __init__(self):
        self.cupPrice = 200

    def makeCoffee(self, coin, cupCount):
        totalPrice = self.cupPrice*cupCount

        if coin < totalPrice:
            return None, None
        else:
            change = coin - totalPrice
            return cupCount, change


class MachineUI:
    def __init__(self):
        self.machine = CoffeMachine()

    def run(self):
        coin = int(input('동전을 입력하세요 : '))
        cup = int(input('몇 잔을 원하세요 : '))

        cupCount, change = self.machine.makeCoffee(coin, cup)

        if cupCount is None:
            print('요금이 부족합니다.')
        else:
            print(f'커피 {cupCount}잔과 잔돈 {change}원')

if __name__ == "__main__":
    ui = MachineUI()
    ui.run()

