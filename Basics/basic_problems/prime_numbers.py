n = 5

count = 0
for i in range(2,n+1):
    if i % n != 0:
         count+=1
        
if count == 1:
     print("prime")
else:
     print("Not prime")