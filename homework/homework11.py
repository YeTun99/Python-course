class Car:
    def __init__(self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.distance = 0
        guess_hour = 0

    def travel_distance(self,mile):
        self.distance+=mile
        print(f"Travel Distance:{self.distance} mile")

    def accelerate(self, mph):
        self.speed += mph
        guess_hour=self.distance/self.speed
        print(f"My car speed is {self.speed} mph now and estimate arrival time {guess_hour} hours")

    
    def brake(self, mph):
        if self.speed -mph >=0:
            self.speed-=mph
            guess_hour=self.distance/self.speed
            print(f"Brake:{mph} Now Speed:{self.speed} and estimate time:{guess_hour} hour")

        else :
            self.speed=0
            print("Now Car stops")
        
my_car = Car("Toyota", "Corolla", 2021, "blue")
print("My Car:",my_car.name,my_car.model,my_car.year,my_car.color)

my_car.travel_distance(392)
my_car.accelerate(20)
my_car.brake(10)
my_car.accelerate(60)
my_car.brake(100)
my_car.accelerate(100)