# 5!= 1x2x3x4x5=120

n=int(input("Enter a number: "))
factorial=1
for i in range(1,n+1):
    factorial*=i
    i+=1    
print(f"Factorial of {n} is {factorial}")