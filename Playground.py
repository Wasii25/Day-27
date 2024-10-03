def add(*args):
    sum= 0
    for n in args:
        sum += n
    return sum


print(add(3,5,4,1,8,2,6,4,5,7,1,4))


def calculate(**kwargs):
    print(kwargs)
    n = 0
    for key,value in kwargs.items():
        print(key,value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw["color"]
        self.seats = kw["seats"]

my_car = Car(make="Volvo", model="Mercedes")