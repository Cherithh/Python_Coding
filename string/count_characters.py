words = "banana"
visited = ""
for i in words:
    if i not in visited:
        print(i,"-->",words.count(i))
        visited+=i