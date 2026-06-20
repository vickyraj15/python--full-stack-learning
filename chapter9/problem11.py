with open("log.txt") as f:
    content = f.read()


with open("newlog.txt", "w") as f:

    f.write(content)
    
