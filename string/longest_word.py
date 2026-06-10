words = "I love python"
longest = ""
for i in words.split():
    if len(i) > len(longest):
        longest = i

print(longest)