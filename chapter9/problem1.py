#write a program to read a file from given  file "poem.txt" and find the output it contain the word 'twinkle'

f=open("poem.txt")
containt =f.read()
if("twinkle" in containt):
    print("twinkle is present in the file")
else:
    print("twinkle is not present in the file")   

f.close