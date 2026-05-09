#  Check if Element Exists

class check:
    def element(self):
        data = input("Enter the list: ")
        our_list = input("Enter the number you want to check: ")
        if our_list in data:
            print(f"Yes your number exists in list :) {our_list}")
        else:
            print(f"Nope your element does'nt exist in list :( {our_list}")

obj = check()
obj.element()