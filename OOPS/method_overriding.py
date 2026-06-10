class Animal:
    def sound(self):
        print("Animal Sound")

class dog(Animal):
    def sound(self):
        print("Dog Barks")

d = dog()
d.sound()