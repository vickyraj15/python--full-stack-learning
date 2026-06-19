import os

# Current directory ka content print karega
contents = os.listdir("./")

print("Contents of directory:")
# Directory ke content ko print karega
for item in contents:
    print(item)