class Employee:
    a =1
    @classmethod # if use the class method then its call class attribute
    def Show(cls):
        print(f"the class atribute is {cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"   
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee() 
e.a = 45 #this is instance atribute 

e.name ="harry khan"

print(e.fname,e.lname)

e.Show()