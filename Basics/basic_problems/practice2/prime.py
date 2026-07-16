# n = 11
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count +=1
# if count <= 2:
#     print("Prime")
# else:
#     print("Not Prime")

count = 0
for i in range(1,50):
    if i > 1:
     for j in range(2,i):
        if i % j == 0:
           break
     else:
        print(i)
