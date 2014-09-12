import dataClass as dc

o = dc.exampleDataClass();
print dir(o);

del o.obj_var
o.new_data = "some_data"
o.f2 = lambda x: x * 3

print dir(o);
print o.new_data
print o.f2("M")
