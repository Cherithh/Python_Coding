words = "I love python"
shortest = words.split()[0]
for i in words.split():
    if len(i) < len(shortest):
        shortest= i

print(shortest)
