#Function to print your name
class name:
    def __init__(self,data):
        self.data = data

    def printing_name(self):
        print("Your name is:",self.data)

obj = name(input("Enter your name: "))
obj.printing_name()