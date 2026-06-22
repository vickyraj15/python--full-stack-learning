from functools import reduce
# map Example
l = [3,4,6,8,4,1,4,]

square =lambda x:x*x

sqlist = map(square,l)
print(list(sqlist))

# Filter example

def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))


# reduce Example

def sum(a,b):
    return a+b

mul=lambda x,y: x*y
print(reduce(mul,l))