print("------------------------------------------------------")
print("First Class Named BMW")
print("------------------------------------------------------")

class Cars:
    Brand = "BMW"
    def __init__(self, Name, Cost, Speed, FuelEconomy):
        self.Name = Name
        self.Cost = Cost
        self.Speed = Speed
        self.FuelEconomy = FuelEconomy
    def accelerate(self):
        return f"{self.Name} is raisng the acceleretion and have reached 140MPH"
    def Braking(self):
        return f"{self.Name} is Breaking now because The Accelration was too high"

# Creating Two Distnct Cat objects from BMW
Car1 = Cars("BMW X7", 100000, 180, 8)
Car2 = Cars("BMW X1", 60000, 140, 15)
print(f"This is {Car1.Name} very Good SUV You can Have at a cost of justs {Car1.Cost}💲 and Reaches Top speed of {Car1.Speed}MPH , and the fuel Economy for this car is grate As Compared its V8 Engine {Car1.FuelEconomy}")
print(f"This is {Car2.Name} very Good Compact You can Have at a cost of just {Car2.Cost}💲 and Reaches Top speed of {Car2.Speed}MPH , and the fuel Economy is Grate in this car {Car2.FuelEconomy}")
print(Car1.accelerate())
print(Car2.accelerate())
print(Car1.Braking())
print(Car2.Braking())

print("------------------------------------------------------")
print("Second Class Named Bikes")
print("------------------------------------------------------")
class Bikes:
    Brand = "Suzuki"

    def __init__(self, Name, Cost, Speed):
        self.Name = Name
        self.Cost = Cost
        self.Speed = Speed
        pass
    def ppf(self):
        return "The Bikes PPF As been Done"

Bike1 = Bikes("Hayabusa", 2100000, 300)
print(f"This is japanise technology Manufactured Bike {Bike1.Name}, And It costs {Bike1.Cost}₹ in India, And on highway it reaches more then {Bike1.Speed}KMPH")
print(Bike1.ppf())