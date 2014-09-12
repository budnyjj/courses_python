def square(x):
    return x ** 2

s = square
print s(5)

def ff(f, x):
    return f(f(x) - 1)

print ff(s, 5)
