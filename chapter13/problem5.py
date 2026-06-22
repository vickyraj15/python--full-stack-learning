from functools import reduce
l =[12,43,57,89,54,21,55,98]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))
