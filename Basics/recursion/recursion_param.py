# Head recursion
# def func(x,y):
#     if y == 0:
#         return
#     print(x)
#     func(x,y-1)

# func(15,5)

# print 1 to N

# # Tail recursion
# def func(i,n):
#     if i > n:
#         return
    
#     func(i+1,n)
#     print(i)

# func(1,10)

# with sum
# def func(sum,i,n):
#     if i > n:
#         print(sum)
#         return
#     func(sum+i,i+1,n)

# func(0,1,5)

# function recursion for sum

def func(n):
    if n==1:
        return 1
    return n + func(n-1)
x = func(5)
print(x)