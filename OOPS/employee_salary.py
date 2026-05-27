class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def yearly_salary(self):
        print(self.name,self.salary)
        print(self.salary * 12 )

Employee1 = Employee("Cherith",20000)
Employee2 = Employee("Mayur",30000)
Employee1.yearly_salary()
Employee2.yearly_salary()