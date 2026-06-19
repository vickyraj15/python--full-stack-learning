f=open("file.txt")
print(f.read())
f.close

#the same can i write using with statement like this

with  open("file.txt") as f:
    print(f.read())

# you dont have a explicetly close the file
