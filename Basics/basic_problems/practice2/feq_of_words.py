words = "Yweriuyerytpio"
for ch in words:
    count = 0
    for x in words:
        if x==ch:
            count+=1
    print(count)