# Count Even and Odd Numbers

class even_odd:
    def counting(self):
        data = input("Enter your numbers: ")
        Even_numbers = 0
        Odd_numbers = 0
        for i in data:
            if int(i) % 2== 0:
                Even_numbers+=1
            else:
                Odd_numbers+=1
        print(f"Number of Even numbers are: {Even_numbers}\nNumber of Odd Numbers are: {Odd_numbers}")

obj = even_odd()
obj.counting()