# Find Duplicate Elements

class finding_dups:
    def dupli(self):
        data = input("Enter your number with spaces: ").split()
        
        duplicates = []
        for i in data:
            if data.count(i) > 1 and i not in duplicates:
             duplicates.append(i)

        print(duplicates)

obj = finding_dups()
obj.dupli()