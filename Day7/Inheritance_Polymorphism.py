## Oops features Inhertance method 
# Class sir made a example 
print("-------------------------------------------------")
print("Class Example for Inheritance")
print("-------------------------------------------------")
class Animals:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} is speaking !!! ")

class dogs(Animals):
    def speak(self):
        print(f"{self.name} is barking") 
Bob = dogs("bob")
Matt = dogs("Matt")
Bob.speak()
Matt.speak()


print("-------------------------------------------------")
print("My exmaple for inheritance")
print("-------------------------------------------------")
## This is my example
# parent class
class Vehicle:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def move(self):
        return f"{self.name} Moving around"

class Fourwheeler(Vehicle):
    def move(self):
        print(f"Hey Bro, Lookout There is a !! {self.brand} {self.name} Going ")

Vehicles1 = Fourwheeler("X7", "BMW")
Vehicles2 = Fourwheeler("Q7", "Audi")
Vehicles1.move()
Vehicles2.move()

## Lets go for polymorphism
print("-------------------------------------------------")
print("class Example for Polymorphism")
print("-------------------------------------------------")
# lets write it then 
def make_animal_speak(Animals):
    return Animals.speak()

class Cat:
    def speak(self):
        print("Meow !!")
class Dog:
    def speak(self):
        print("Bark !!")

cat = Cat()
dog = Dog()
make_animal_speak(cat)
make_animal_speak(dog)

print("-------------------------------------------------")
print("My exmaple for Polymorphism")
print("-------------------------------------------------")
def make_vehicles_move(Vehicles):
    return Vehicles.move()

class twowheelers:
    def move(self):
        print("Hayabusa")
    
class Suv:
    def move(self):
        print("XUV500")

bike = twowheelers()
suv = Suv()
make_vehicles_move(bike)
make_vehicles_move(suv)
