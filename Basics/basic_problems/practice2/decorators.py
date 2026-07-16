
def greater_first(func):
    def wrap(a,b):
        if a < b:
            a , b = b , a
        return (func(a,b))
    return wrap


@greater_first
def add(a,b):
    return a + b
@greater_first
def sub(a,b):
    return a - b
# @greater_first
def div(a,b):
    return a / b

# add = greater_first(add)
# sub = greater_first(sub)
div = greater_first(div)
print(add(2,3))
print(sub(2,3))
print(div(2,3))