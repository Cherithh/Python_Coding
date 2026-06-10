class Father:
    def money(self):
        print("Father's Money")
    
class Mother:
    def care(self):
        print("Mother's Care")

class child(Father,Mother):
    pass

c = child()
c.money()
c.care()