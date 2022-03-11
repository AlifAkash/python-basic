colors = [11, 34, 98, 43, 45, 54, 54]
for digit in colors:
    if digit > 50 :
        print(digit)


colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for integer in colors:
    if isinstance(integer, int):
        print(integer)


colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for integer in colors:
    if isinstance(integer, int) and integer > 50:
        print(integer)