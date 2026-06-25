# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else :
#         return n * factorial(n-1)
    

# print(factorial(5))

def countdown(n):
    if n == 0:
        print("Done")
        return 0

    print(n)
    countdown(n-1)

countdown(10)


# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     return fibonacci(n-1)  + fibonacci(n-2)

# for i in range(10):
#     print(fibonacci(i),end="")