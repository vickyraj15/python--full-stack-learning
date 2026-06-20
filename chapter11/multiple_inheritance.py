class Employee:
    company = "ITC"
    name ="default name"
    def show(self):
        print(f"NAme of Employee is {self.name} and the company is {self.company}")
class Coder:
    language = "python"
    def printLanguage(self):
        print(f"out of the all the languages here is your language:{self.language}")

class Programmer(Employee,Coder):
    campany = "ITC Infotech"   
    def showLangauge(self):   
        print(f"the name is:{self.campany} and he is good with {self.language} language")   

a = Employee()
b= Programmer()

b.show()
b.printLanguage()
b.showLangauge()
