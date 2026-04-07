class Car:
    handle = 1
    speed = 0

    def __init__(self, name, speed):        
        self.name = name        # 현재 객체의 name 에게 name(지역변수) 인자값 치환 
        self.speed = speed

    def showData(self):         # 멤버 메소드
        km = "킬로미터"
        msg = "속도" + str(self.speed) + km
        return msg
    
    def printHandle(self):
        return self.handle
    
print(Car.handle)       # 원형(prototype) 클래스의 멤버 호출, 원형 클래스 또한 하나의 객체
car1 = Car("tom", 10)   # 생성자 호출 후 객체 생성(인스턴스화)
print("car1 객체 주소 :", car1)
print("car1 :", car1.name, " ", car1.speed, car1.handle)        # 객체에 없다면 원형을 참조 원형은 공유 멤버
car1.color = "파랑"
print('car1.color :', car1.color)       # 원형 클래스에는 없지만 이 객체에만 멤버가 추가, 각각의 객체마다 고유의 멤버 생성 가능 

car2 = Car("john", 20)      # 생성자 호출 후 객체 생성
print("car2 객체 주소 :", car2)
print("car2 :", car2.name, " ", car2.speed, car2.handle)

# print(Car.color, " ", car2.color)       # ttributeError: type object 'Car' has no attribute 'color'  car1에서만 color 멤버를 정의 
print()
print(id(Car), id(car1), id(car2))      # 원형 과 각 객체는 모두 다른 주소 값을 가짐
print(car1.__dict__)        # 객체의 멤버 확인, 각 객체마다 멤버도 다를 수 있음
print(car2.__dict__)

print("-------메소드-----------")
print("car1 speed :", car1.showData())
print("car2 speed :", car2.showData())

car1.speed = 80
car2.speed = 110
print("car1 speed :", car1.showData())
print("car2 speed :", car2.showData())

print("car1 handle :", car1.printHandle())
print("car2 handle :", car2.printHandle())


