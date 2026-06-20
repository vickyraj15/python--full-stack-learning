with open("log.txt") as f:
    content= f.read()

if("python" in content):
    print("ues python is present in content ")  
else:
    print("no python os n ot present in content")      