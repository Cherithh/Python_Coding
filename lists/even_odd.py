# Identify Even and Odd Numbers

class even_odd:
    def counting(self):
        data = [1,2,3,4,5,6,7,8,9]
        Even_numbers =[]
        Odd_numbers = []
        for i in data:
            if i % 2== 0:
                Even_numbers.append(i)
            else:
                Odd_numbers.append(i)
        print(f"Number of Even numbers are: {Even_numbers}\nNumber of Odd Numbers are: {Odd_numbers}")

obj = even_odd()
obj.counting()