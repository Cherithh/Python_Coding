# Reverse a number

num = int(input("Enter your number: "))
rev = 0
while num >0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
if rev == num[::-1]:
      print("Palindrome",rev)
else:
       ("not palindrome")