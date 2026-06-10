# largest number

lst = [1,2,3,4,5]

largest = lst[0]

for i in lst:
    if i < largest:
        largest= i

print(largest)