words = "AuTOmAtiON"
uppercase = 0
lowercase = 0
for i in words:
    if i.islower():
     lowercase+=1
    elif i.isupper():
       uppercase+=1
    else:
       print("Not an alphabet")
print("Uppercase: ",uppercase)
print("Lowercase: ",lowercase)