class Employee: # this is class 

    language ="pyton" # this is a class attribute
    salary = 130000

    def __init__(self,name,salary,language): #dunder method which is automatically called
         self.name = name
         self.salary = salary
         self.salary = language
         print("I am creating an object")



    def getInfo(self):  
        print(f"the language is {self.language}.this  salary is {self.salary}")

  



    @staticmethod # if I not any use property of then I use staticmenthod. now i clear the self then coming any error

    def greet(): # this is method and function, all method is called a function but all function is not call method 
     print("good morning")     


vicky =Employee("vicky raj","javascript",130000)
print(vicky.name,vicky.language,vicky.salary)
# vicky.language = "javascript" #This is an instance attribute 

# vicky.getInfo()
# vicky.greet()