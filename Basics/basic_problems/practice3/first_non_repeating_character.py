words = "aabbccddefg"
result = ""
for ch in words:
    if words.count(ch) == 1:
        result+=ch
        print(ch)
        break