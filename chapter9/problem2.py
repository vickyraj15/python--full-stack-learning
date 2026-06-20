import random


def game():
    print("you are the playing the game..")
    score = random.randint(1,62)
# fatch the hiscore
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"your score:{score}")  
    if(hiscore>score): 
        # write the hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score
  
game()


