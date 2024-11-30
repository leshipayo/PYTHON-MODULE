# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses should implement this method")

# Subclass 1 - Car
class Car(Vehicle):
    def move(self):
        print("Driving ")

# Subclass 2 - Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ")

# Subclass 3 - Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ")
#Subclass 4-Bicycle
class Bicycle(Vehicle):
    def move(self):
         print("cycling")

# Creating instances of the classes
car = Car()
plane = Plane()
boat = Boat()
Bicycle=Bicycle()

# Calling the move() method on each instance
car.move()   
plane.move()
boat.move()
Bicycle.move()
