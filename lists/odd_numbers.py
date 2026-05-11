# Return Only Odd Numbers

class odd_numbers:
    def odd(self):
        data = input("Enter your numbers and give spaces when you enter!").split()
        odds = []
        for i in data:
            if int(i) %2 != 0:
                odds.append(i)
        
        print("Odd numbers in the list you've given:",odds)


obj = odd_numbers()
obj.odd()
