import dataClass as dc

o1 = dc.exampleDataClass();
o2 = dc.exampleDataClass();

print "Data is object data member:"
print "BEFORE:"
print "o1.cls_var:", o1.cls_var
print "o2.cls_var:", o2.cls_var

dc.exampleDataClass.cls_var =\
"new_object_data"

print "AFTER:"
print "o1.cls_var: ", o1.cls_var
print "o2.cls_var:", o2.cls_var
