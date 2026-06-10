# Remove Duplicates
# class Duplicates:

#     def dupli(self):

#         data = input("Enter your numbers: ").split()

#         unique = []

#         for i in data:

#             if i not in unique:
#                 unique.append(i)

#         print("After removing duplicates:", unique)

# duplicate = Duplicates()

# duplicate.dupli()


# Finding duplicates

# lst = [1,2,3,4,5,3,2,1]

# duplicates = []

# for i in lst:
#     if lst.count(i) > 1 and i not in duplicates:
#         duplicates.append(i)

# print(duplicates)


nums = [1,2,3,4,5,6,4,3,1]
unique = []

for i in nums:
    if i not in unique:
        unique.append(i)
    if i == 1 or i == 2:
        unique.remove(i)

print(unique)