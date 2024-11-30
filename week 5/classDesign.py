# Class for an individual Car
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        print(" New Arrivalls from Germany")
    def update_cost(self,cost):
        print("calculating cost")
        self.cost=cost

print(cars)

c = Car ("BMW","3 Series","2024","blue")
print(c.brand,c.model,c.year,c.color)


c = Car ("Toyota","Harrier","2024","White")
print(c.brand,c.model,c.year,c.color)


c = Car ("Tesla","Model 3","2024","Midnight Silver")
print(c.brand,c.model,c.year,c.color)

#list
cars=[Car ("Toyota","Harrier","2024","White"),Car ("BMW","3 Series","2024","blue"),Car ("Tesla","Model 3","2024","Midnight Silver")]
print(cars[1].brand)