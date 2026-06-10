words = "i love python"
replaced_words = []

for i in words.split():
    replaced_words.append(i)

print("-".join(replaced_words))