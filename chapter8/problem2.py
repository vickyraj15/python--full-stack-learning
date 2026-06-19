def f_to_c(f):
    
    return (f-32)*5/9

f=int(input("Enter temperature in fahrenheit: "))
c=f_to_c(f)
print(f"{round(c,2)} °c")