items = [("one", 1), ("two", 2), ("three", 3)]

total = reduce(lambda a, b:\
               (0, a[1] + b[1]),items)[1]

print total
