myFile = open("file/fruit.txt")
print(myFile.read()) #read method execute only once
myFile.close()

with open("file/fruits2.txt") as file:
    content = file.read()

print(content)

with open("file/bear.txt") as file:
    content = file.read()
    print(content[:90]) #read first 90 words