class Employee:
    company = "ITC"
    def show(self):
        print(f"NAme of Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     campany = "ITC Infotech"   
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")    


#     def showLangauge():   
#         print(f"the name is:{self.name} and he is good with {self.language} language")    

class Programmer(Employee):
    campany = "ITC Infotech"   
    def showLangauge():   
        print(f"the name is:{self.name} and he is good with {self.language} language")   

a = Employee()
b= Programmer()

print(a.company,b.campany)
