# count words in a file
with open('myfile2.txt','r') as f:
      count = 0
      for line in f:
        count += 1
      print(count)