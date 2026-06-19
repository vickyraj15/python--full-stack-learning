# def rem(l, word):
#     if(word in l):
#         l.remove(word)
#     return l
def rem(l, word):
    n=[]
    for item in l:
        if(item!=word):
            n.append(item.strip(word))
    return n

   




l = ["herry", "vicky", "rohan", "jerry", "berry","an"]
print(rem(l, "an"))