f=open("file.txt") # open the file 
print(f.read())   #read and print   the file 
f.close     #close file 

#the same can i write using with statement like this

with  open("file.txt") as f:
    print(f.read())

# you dont have a explicetly close the file
