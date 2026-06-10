# with open("Newfile.txt","w") as f:
#     f.write("Hi this is a new file")

# with open("Newfile.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("Newfile.txt","a") as f:
#     f.write("\nAnd i appended a file")

# with open("Newfile.txt","r") as f:
#     data = f.read()
#     print(data)

# count lines
# with open("Newfile.txt","r") as f:
#     count = 0

#     for line in f:
#         count+= 1
#     print(count)

# count words
with open("Newfile.txt","r") as f:
    data = f.read()
    data1 = data.split()
    print(len(data1))