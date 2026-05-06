#Count Words in File
with open("myfile.txt",'r') as f:
    data = f.read()
    words = data.split()
    print(len(words))