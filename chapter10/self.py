class Employee: # this is class 

    language ="pyton" # this is a class attribute
    salary = 50000

    def getInfo(self):  
        print(f"the language is {self.language}.this  salary is {self.salary}")

  
    @staticmethod # if I not any use property of then I use staticmenthod. now i clear the self then coming any error

    def greet(): # this is method and function, all method is called a function but all function is not call method 
     print("good morning")     


vicky =Employee()
vicky.language = "javascript" #This is an instance attribute 
#
vicky.getInfo()
vicky.greet()