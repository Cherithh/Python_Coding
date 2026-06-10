# Upper half

for i in range(8):
    for j in range(8-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
#  Lower half
for i in range(8,0,-1):
     for j in range(8-i):
        print(" ",end="")
     for k in range(2*i-1):
        print("*",end="")
     print()
