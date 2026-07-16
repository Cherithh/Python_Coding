# words = "Cherith"
# freq={}
# for ch in words:
#     if ch not in freq:
#         freq[ch] = 1
#     elif ch in freq:
#         freq[ch] +=1


# print(freq)

words = "Cherith"
freq = {}
for ch in words:
    freq[ch] = freq.get(ch,0) + 1

print(freq)