try:
    a = int(input("Hey, Enter the number :"))

    print(a)



except Exception as e:
    print(e)

finally:
    print("I am inside of Finally")