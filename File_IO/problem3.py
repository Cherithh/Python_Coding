with open("myfile.txt",'r') as f:
    data = f.read()
    words = data.replace(" ","")
    print("Total Characters: ",len(words))