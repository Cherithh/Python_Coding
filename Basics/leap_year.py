# count consonents

words = "consonants"
count  = 0

for i in words:
    if i not in "aeiou":
        count+=1

print(count)