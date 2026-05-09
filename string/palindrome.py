#check for palindrome

data = input("Enter the word: ")
class palindrome:
    def palin(self):
        if data == data[::-1]:
            print("Yes, its palindrome")
        else:
            print("Nope, not palindrome")

pal = palindrome()
pal.palin()