# Remove Duplicates
class Duplicates:

    def dupli(self):

        data = input("Enter your numbers: ").split()

        unique = []

        for i in data:

            if i not in unique:
                unique.append(i)

        print("After removing duplicates:", unique)

duplicate = Duplicates()

duplicate.dupli()