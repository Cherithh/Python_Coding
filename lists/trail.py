lst1 = [1,2,3,4,5]
lst2 = [5,7,4,3,1]
common = []

for i in lst1:
    if i in lst2:
        common.append(i)

print(common)