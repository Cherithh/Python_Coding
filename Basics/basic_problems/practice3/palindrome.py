# num = 1333
# n = num
# rev = 0

# while n > 0:
#     ld = n % 10
#     rev = (rev * 10) + ld
#     n = n //10

# if rev == num:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
words = "mada"
if words == words[::-1]:
    print("Palindrome")
else:
    print("Not Palidrome")