name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today"

message = "Hello %s %s" % (name, surname) #older version
message2 = f"Hello {name} {surname}. Whats up {when}"

print(message)
print(message2)