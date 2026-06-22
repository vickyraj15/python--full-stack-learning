def division5(n):
    if(n%5==0):
        return True
    return False

a = [122, 25,525,678,335,552,725,625,125,300]

f = list(filter(division5 ,a))

print(f)