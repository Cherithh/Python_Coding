# Check for palindrome number

num = input("Enter your number: ")
if num == num[::-1]:
    print("Its Palindrome")
else:
    print("Its not Palindrome")