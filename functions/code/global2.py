name = "Jack"

def f(self):
   # global name 
   name = "Robert"
   print "Within function", name
   print locals()
   print globals()
   print self.name


print "Outside function", name
f()
print "Outside function", name
