# n = 101

# rev = 0
# total = 0
# while n > 0:
#     rev = n % 10
#     total = total * 10 + rev
#     n = n // 10
# print(total)
# if total == n:
#     print("Palindrome")
# else:
#     print("No")
    

# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact *= i

# print(fact)



# for num in range(1,51):
#     count  = 0

#     for i in range(1,num+1):
#      if num % i == 0:
#         count+= 1
#     if count == 2:
#         print(num)


# a = 0
# b = 1

# print(a)
# print(b)


# for i in range(1,6):
#     c = a + b
#     print(c)

#     a = b 
#     b = c


# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# nums = [23,43,54,6,78]
# largest = nums[0]
# for i in nums:
#     if i > largest:
#         largest = i
# print(largest)

# text = "qwertyuio"

# count = 0

# for i in text:
#     if i in "aeiou":
#         count+=1
# print(count)

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()