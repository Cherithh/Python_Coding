# num = 13
# numbers = 0
# for i in range(1,100):
#     if i % num == 0:
#         print(i)


# num = 15

# numbers = []
# for i in range(1,100):
#     if i % num == 0:
#         numbers.append(i)

# print(numbers)

l = [15, 38, 46, 68, 75, 90]

result = list(filter(lambda x : x % 15 == 0,l))
print(result)