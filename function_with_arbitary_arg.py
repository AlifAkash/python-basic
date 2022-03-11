#non_keyword
def mean(*args):
    print(type(args))
    return sum(args) / len(args)

print(mean(7, 5, 6, 2))

#keyword
def mean(**kwargs):
    print(type(kwargs))
    return sum(kwargs.values()) / len(kwargs)

print(mean(a=7, b=5, c=6, d=2))
