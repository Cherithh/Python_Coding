# add = lambda a ,b : a + b
# print(add(10,20))


students = [("Goku",99),("Zoro",90),("Cherith",80)]

students.sort(key=lambda student:student[1])

print(students)