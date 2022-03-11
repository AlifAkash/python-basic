import time
import os

while True:
    if os.path.exists("file/vegis.txt"):
        with open("file/vegis.txt") as file:
            print(file.read())
    else:
        print("file does not exists")
    time.sleep(10)
