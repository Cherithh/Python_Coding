count = 0

def func():
    global count
    if count == 4:
        return
    print("Cherith")
    count+=1
    func()
func()
    

# func()

# Tail recursion
# count = 0

# def func():
#     global count
#     if count == 4:
#         return
    
#     count+=1
#     func()
#     print("Cherith")

# func()