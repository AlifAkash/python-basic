with open("file/vagitables.txt", "a+") as file:
    file.write("\nBeetroot")
    file.seek(0)
    content = file.read()

print(content)