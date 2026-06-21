try:
    a = int(input("Hey, Enter the number :"))

except ValueError as v:
    print("heyy")
    print(v)    

except Exception as e:
    print(e)

print("thank you")        