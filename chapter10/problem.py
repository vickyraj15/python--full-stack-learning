class Programmer:
    company ="macrosoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer("vicky",120000,801303)    
print(p.name,p.pin,p.salary,p.company)  
r =Programmer("rahul",130000,803116)
print(r.name,r.pin,r.salary,r.company)  
        