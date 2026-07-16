arr = [0,5,0,3,2,0]
arr1 = []

for num in arr:
    if num != 0:
        arr1.append(num)

len = len(arr) - len(arr1)

for i in range(1,len+1):
    arr1.append(0)

print(arr1)