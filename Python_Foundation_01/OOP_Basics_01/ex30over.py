# 오버라이딩 : 결제 시스템

class Payment:      # 공통 규칙 선언 
    def pay(self, amount):
        print(f"{amount}원 결제 처리")

# Payment의 자식은 결제를 pay라는 동일 메소드를 이용하기를 기대
# 동일 인터페이스 구사

class CardPayment(Payment):
    # 얘만의 고유 멤버 ....
    # 고유 메소드 ....

    def pay(self, amount):         
        print(f"{amount}원 카드결제 승인 완료")

class CashClass(Payment):
    # .....

    def pay(self, amount):         
        print(f"{amount}원 현금결제 완료 - 감사합니다.")

payments = [CardPayment(), CashClass()]

for p in payments:
    p.pay(5000)         # 다형성

        
