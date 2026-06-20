from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def Book(self,fro,to):
        print(f"Ticket is book in train no: {self.trainNo} from {fro} to {to}") 

    def getStatus(self):
        print(f"train no:{self.trainNo} is runing on time")    


    def getFare(self ,fro,to) :
        print(f"ticket fare in train no:{self.trainNo} from {fro} to {to} is {randint(2222, 5555)}")  

t = Train(12399)  
t.Book("rampur","delhi")   
t.getStatus()   
t.getFare("Rampur ","delhi") 
  