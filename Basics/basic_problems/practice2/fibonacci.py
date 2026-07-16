fib = 10

a = 0
b = 1

for i in range(1,fib+1):

    print(a,end=" ")

    c = a + b
    a = b
    b = c