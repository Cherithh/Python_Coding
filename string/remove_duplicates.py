words = "Monitor"
duplicates = ""
for i in words:
    if i not in duplicates:
        duplicates+=i
print(duplicates)