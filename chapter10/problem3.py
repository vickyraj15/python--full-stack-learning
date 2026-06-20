class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"the squre is {self.n * self.n}")

    def cube(self):
         print(f"the cube is {self.n * self.n *self.n}") 

    def squareroot(self):
        print(f"the squreroot is {self.n **1/2}")  

    @staticmethod
    def hello():
        print("hello there")    

   


a = Calculator(4)  
a.hello()
a.square() 
a.cube()
a.squareroot()     