class Employee:
    a =1
    @classmethod # if use the class method then its call class attribute
    def Show(cls):
        print(f"the class atribute is {cls.a}")


e = Employee() 
e.a = 45 #this is instance atribute 

e.Show()

