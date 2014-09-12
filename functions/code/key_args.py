def display(**details):
   # print "ARGS:"
   # for i in args:
   #    print i

   # print "kwargs:"
   # for i in details:
   #    print "%s: %s" % (i, details[i])
   d = [43, "Lary", "M"]
   (x, y, z) = d
   print x, y, z

def display2(age, name, sex):
   print "DISPLAY"
   print age, name, sex

display(age=43, name="Lary", sex="M")
