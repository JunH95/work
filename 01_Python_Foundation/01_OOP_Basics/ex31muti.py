# 클래스의 다중 상속 - 부모가 복수 

class Tiger:
    data = "호랑이 세계"

    def cry(self):
        print("호랑이 : 어흥")
    
    def eat(self):
        print("맹수는 고기를 좋아함")

class Lion:
    def cry(self):
        print("사자 : 으르렁")

    def hobby(self):
        print("백수의 왕 : 낮잠이 취미")
    

# 두 부모 클래스에 같은 메소드가 있을 때 다중 상속 받는 자식은 어떤 메소드를 받아야 하는지
class Liger1(Tiger, Lion):  # 다중 상속은 순서가 중요, 메소드 중복 시 먼저 들어온 부모의 메소트를 받음
    pass 

a1 = Liger1()
print(a1.data)
a1.eat()
a1.hobby()
a1.cry()
print("-----------")
def hobby():
    print("모듈의 멤버 : 일반 함수")

class Liger2(Lion, Tiger):
    data = "라이거 만세"    # hiding(shadowing)

    def play(self):
        print("라이거 고유 메소드")

    def hobby(self):        # 메소드 오버라이딩
        print("라이거는 공원 걷기를 좋아함")
    
    def showData(self):
        self.hobby()        # 동일 클래스 내
        super().hobby()     # 부모 클래스
        hobby()             # 모듈의 멤버

        self.eat()
        super().eat()

        print(self.data + " " + super().data)

a2 = Liger2()
a2.cry()  
a2.showData()

