def modify(string, lst):
    string = "new " + string
    for idx, val in enumerate(lst):
        lst[idx] = "new " + val

names = ["cat", "book", "cinema"]
s = "machine"

print "BEFORE MODIFY()"
print names
print s

modify(s, names)

print "AFTER MODIFY()"
print names
print s
