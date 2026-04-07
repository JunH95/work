class ElecProduct:
    volume = 0
    
    def volumeControl(self, volume):
        print(f"전자제품의 음량 : {volume}")

class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        print(f"Tv 음량 : {volume}")

class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        print(f"Radio 음량 : {volume}")

elecproduct = [ElecTv(), ElecRadio()]

for e in elecproduct:
    e.volumeControl(30)

product = ElecProduct()
tv = ElecTv()
product = tv
product.volumeControl(5)

radio = ElecRadio()
product = radio
product.volumeControl(3)


class Animal:
    def move(self):
        pass

class Dog(Animal):
    name = "개"

class Cat(Animal):
    name = "고양이"

class Wolf(Dog, Cat):
    pass

class Fox(Cat, Dog):
    def foxMethod(self):
        print('Fox 고유 메소드')

dog1 = Dog()
dog1.move()

