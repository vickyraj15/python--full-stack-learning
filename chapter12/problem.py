try:
    with open("file.txt") as f:
     print(f.read())

except Exception as e:
   print(e)


try:
   with open("file1.txt") as f:
    print(f.read())

except Exception as e:
   print(e)


try:
   with open("file2.txt") as f:
     print(f.read())

except Exception as e:
   print(e)


print("thanku for run program")
