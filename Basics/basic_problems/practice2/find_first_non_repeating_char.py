words = "aabbccdsdfg"
result = ""
non_repeated_char = ""
for ch in words:
    if words.count(ch) == 1:
        result+=ch
        break
    

print(result)