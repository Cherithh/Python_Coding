#Replace Word in File
with open("good_bad.txt",'r') as f:
    data = f.read()

data = data.replace("bad","good")

with open("good_bad.txt",'w') as f:
    f.write(data)
    