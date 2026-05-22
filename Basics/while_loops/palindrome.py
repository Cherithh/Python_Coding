# # Palindrome using while

# words = input("Enter the word to check for palindrome: ")
# rev = ""
# i = len(words) - 1
# while i >= 0:
#     rev = rev + words[i]
#     i -= 1
# if rev == words:
#     print("Its a Palindrome")
# else:
#     print("Its not palindrome")

import requests

response = requests.get("https://reqres.in/api/users/2")

print(response.status_code)
print(response.json())
