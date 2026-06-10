word = "Automation"
repeated = ""
for i in word.lower():
    if word.count(i) == 2:
        print(i)
        break