'''
1 for snake
-1 for water
0 for gun

'''
import random
computer = random.choice([1,0.-1])
yourstr= input("enter your choice")
youDist = {"s":1, "w":-1, "g":0}

reverseDist = {1:"snake",-1:"water",0:"gun"}

you = youDist[yourstr]
#v=by now two number you and computer
print(f"you choose{reverseDist[you]}\n computer chose{reverseDist[computer]}")

if(computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("you lose the game")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you ==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")    
    else:
        print("something went wrong")



    

    