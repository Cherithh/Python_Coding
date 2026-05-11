# Check for vowels

data = input("Enter the words: ").lower()
class vowels:
    def vow(self):
        count = 0
        for i in data:
            if i in "aeiou":
                count+=1
        print(count)
                
vowi = vowels()
vowi.vow()