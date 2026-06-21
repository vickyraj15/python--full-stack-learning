a = int(input("enter the numeber:"))
b = int(input("enter the second number:"))

if(b==0):
    raise ZeroDivisionError("heyy, your program is not meant to divide number by zero")
else:
    print(f"the division a/b is : {a/b}")