# 65pythan lambda
def x(a): return a+10


print(x(5))


def y(b): return b+19


print(y(6))
# multiply
def x(a, b): return a*b


print(x(8, 9))
# 4
def x(a, b): return a*b


print(x(6, 3))
# 356
def x(a, b, c): return a+b+c


print(x(6, 8, 7))
# 45
def x(a, c): return a//c


print(x(8, 2))
# 544


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler)
