lowercase = lambda x: x.lower()
print_assign = lambda name, value:\
               name + '=' + str(value);name
adder = lambda x, y: x+y

print lowercase("tau")
print print_assign("a", 2)
print adder(2, 3)
