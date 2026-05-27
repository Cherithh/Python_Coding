class Car:
    def __init__(self,brand,model,colour):
        self.brand = brand
        self.model = model
        self.colour = colour

car1 = Car("Nissan","Skyline GTR34","Silver/Blue")
car2 = Car("Toyota","Supra","Orange")
print(car1.brand,car1.model,car1.colour)
print(car2.brand,car2.model,car2.colour)