punc = '''!@#$%^&*()?/><.,:;"'|\}{[]-=}'''

word = input("Enter anything here: ")
word1 = ""
for ch in word:
    if ch not in punc:
        word1+=ch
print(word1)