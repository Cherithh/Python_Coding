word1 = "earth"
word2 = "heart"

if len(word1) != len(word2):
    print("Not Anagram")
else:
    for i in word1:
        if word1.count(i) != word2.count(i):
            print("Not Anagram")
            break   
    else:
        print("Anagram")