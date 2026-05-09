data = input("Enter the words: ")
count = 0
class vowels:
    def vow(self):
        count = 0
        for i in data:
            if i in "aeiou":
                count+=1
        print(count)
                
vowi = vowels()
vowi.vow()