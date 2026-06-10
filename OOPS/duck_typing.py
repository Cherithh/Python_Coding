class Dog:

    def speak(self):
        print("Dog barks")


class Cat:

    def speak(self):
        print("Cat meows")


class Human:

    def speak(self):
        print("Human talks")


def make_sound(obj):
    obj.speak()


d = Dog()
c = Cat()
h = Human()

make_sound(d)
make_sound(c)
make_sound(h)