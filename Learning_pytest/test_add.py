class testAddition:
    def add(self,a,b):
        return a + b
    
    def test_add(self):
         assert self.add(5,4) == 9