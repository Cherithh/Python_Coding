class A:
    def classa(self):
        print("Inheriting class A")

class B(A):
    def classb(self):
        print("Inheriting class B")

class C(A):
    def classc(self):
        print("Inheriting class C")

class D(B,C):
    def classd(self):
        print("Inheriting class D")

d = D()
d.classa()

