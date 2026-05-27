class Student:
    def __init__(self,name,sem,marks):
        self.name = name
        self.sem = sem
        self.marks = marks

    def display(self):
        print(self.name,self.sem,self.marks)

Student1 = Student("BrainOConner",4,95)
Student2 = Student("Dom",6,90)
Student1.display()
Student2.display()
