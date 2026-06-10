class Animal:
    def sound(self):
        print("Animal Sound")

class dog(Animal):
    pass

class cat(Animal):
    pass

d =dog()
d.sound()

c = cat()
c.sound()