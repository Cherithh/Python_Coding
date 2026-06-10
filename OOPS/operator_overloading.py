class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary


e1 = Employee(10000)
e2 = Employee(20000)

print(e1 + e2)