nums = [1,2,3,4,5,6,7,8,9,10]

for num in nums:
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count+=1

    if count == 2:
        print(num,"Isprime")
    else:
        print(num,"Isnotprime")