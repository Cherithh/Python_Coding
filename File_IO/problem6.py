#Find Longest Word in File

with open("myfile.txt",'r') as f:
    data = f.read()
    words = data.split()
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print("Longest word:",longest_word)