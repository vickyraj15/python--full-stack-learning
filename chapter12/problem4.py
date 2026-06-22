n = int(input("enter the number:"))

table = [n *i for i in range(1,11)]

with open("table.txt","a") as f:
    f.write(str(table) + "\n")
     