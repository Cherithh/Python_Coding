#Write User Input to File
with open("myfile.txt",'w') as f:
    f.write((input("Enter what you want to write: ")))