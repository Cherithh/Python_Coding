student = {"name" : "Cherith","Class" : 10,"Age" : 25, "Gender" : "Male"}
student["City"] = "Mysore"
student.update({"Age" : 24})
print(student.keys())
print(student.values())
print(student.items())

for key , value in student.items():
    print(key,value)