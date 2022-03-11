def area(a, b):
    return a * b

print(area(4, 5))

#default argument
def area(a, b=7):
    return a * b

print(area(4))
#keyward arg
print(area(b=5, a=6))