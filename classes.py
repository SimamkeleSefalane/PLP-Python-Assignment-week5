class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

class Animal:
    def move(self):
        print("Walking")

# Creating objects
car = Car()
plane = Plane()
boat = Boat()
animal = Animal()

# Calling move() on each object
for obj in [car, plane, boat, animal]:
    obj.move()
