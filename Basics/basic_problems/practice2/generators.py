
def nums():
    for i in range(100):
        yield i 
n = nums()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))