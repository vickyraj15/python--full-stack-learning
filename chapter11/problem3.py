class Employee:
   # if I create class properties then like thius type
   salary =1300
   increment = 20 
   @property
   def salaryAfterIncrement(self):
      return (self.salary + self.salary * (self.increment/100))

   @salaryAfterIncrement.setter
   def salaryAfterIncrement(self,salary):
      self.increment  = ((salary/self.salary) -1)*100 
   

e = Employee()  
#if I create instance propeties them write like this 
# e.salary =1300
# e.increment = 20
e.salaryAfterIncrement =1560
print(e.increment)