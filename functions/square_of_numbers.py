#Function to find square of a number
class square_root:
      def __init__(self,a):
        self.a = a
    
      def square(self):
        return self.a ** 2
      
      def output(self):
        print(f"Sum of {self.a} is {self.square()}")

obj = square_root(7)
obj.output()