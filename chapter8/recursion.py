'''
factorial(0)=1
factorial(1)=1
factorial(2)=2x1
factorial(3)=3x2x1
factorial(4)=4x3x2x1
factorial(5)=5x4x3x2x1
factorial(n)=n x (n-1) x (n-2) x (n-3) x ... x 3 x 2 x 1
factorial(n)=n x factorial(n-1)
'''

def factorial(n):
    if n==0 or n==1:
        return 1
    
    return n*factorial(n-1)
n=int(input("Enter a number: "))
print(f"factorial number is:{factorial(n)}")
