import dataClass as dc

o1 = dc.exampleDataClass();
o2 = dc.exampleDataClass();

print "Data is object data member:"
print "BEFORE:"
print "o1.obj_var: ", o1.obj_var
print "o2.obj_var:", o2.obj_var

o1.obj_var = "new_object_data"

print "AFTER:"
print "o1.obj_var: ", o1.obj_var
print "o2.obj_var:", o2.obj_var
