myFile = open("file/fruit.txt")
content = myFile.read()
myFile.close()
print(content)
print(content)

with open("file/fruits2.txt") as file:
    content = file.read()

print(content)
