# 추상 클래스(abstract class)
# 추상 메소드를 가진 클래스를 추상 클래스라고 하며
# 얘는 인스턴스 할 수 없다. 객체 생성 불가
# 부모 클래스로만 사용됨


from abc import *


class AbstractClass(metaclass=ABCMeta):  #추상클래스

    @abstractmethod
    def abcMethod(self):     #추상메소드
        pass

    def normalMethod(self):  #일반메소드
        print('추상클래스 내의 일반 메소드')

#parent = AbstractClass()    #에러:추상클래스는 객체 생성 불가

class Child1(AbstractClass):   #상속   부모의 추상 메소드 오버라이딩 안하면 자식도 추상클래스가 됨
    name = '난 Child1'

    def abcMethod(self):    #선언 강요
        print('추상 메소드를 오버라이드함')


class Child2(AbstractClass):   #상속
    def abcMethod(self):    #선언 강요
        print('추상 메소드를 Child2에서도 오버라이드함')

    def normalMethod(self):  #선언 선택적
        print('추상클래스 내의 일반 메소드를 오버라이드함')


c1 = Child1()            #생성된 객체의 주소를 치환
print(c1.name)

c1.abcMethod()          #Bound Method call
c1.normalMethod()


print()

c2 = Child2             #클래스를 치환
c2.abcMethod(c2)        #UnBound Method call
c2.normalMethod(c2)


print('\n다형성 -----')
parent = AbstractClass   #추상클래스 타입의 변수 선언은 가능
print(type(parent))
parent = c1
parent.abcMethod()
parent.normalMethod()  #추상클래스의 메소드 수행
print()

parent = c2
parent.abcMethod(parent)
parent.normalMethod(c2)  #자식클래스의 메소드 수행