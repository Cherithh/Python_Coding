# pattern programming

for i in range(1,6):

    # Spaces
    for j in range(5-i):
        print(" ",end="")

    # Stars
    for k in range(2 * i - 1):
        print("*",end="")

    print()