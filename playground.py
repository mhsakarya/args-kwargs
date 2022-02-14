def add(*args):
    result = 0
    for each in args:
        result += each
    return result


print(add(1,2,3,4,5,6,7))

def calculate(**kwargs):
    return kwargs




print(type(calculate(a=1,b=2)))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        #dictionary[] key value belirtmek yerine, get metodu isim argument i verilmediğinde None döndürür

my_car = Car(make="Nissan")
print(my_car.model)


