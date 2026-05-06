#Count Vowels in File

with open("myfile.txt") as f:
    data = f.read().lower()
count = 0

for ch in data:
    if ch in 'aeiou':
        count+= 1

print(count)