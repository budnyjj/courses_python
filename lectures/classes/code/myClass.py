class exampleDataClass:
    """A data example class"""
    cls_var = "old_class_data"

    def __init__(self):
        self.obj_var = "old_object_data"
    def f(self):
        return self.obj_var

dc1 = exampleDataClass();
dc2 = exampleDataClass();

print "Data is object data member:"
print "BEFORE:"
print "dc1.obj_var: ", dc1.obj_var
print "dc2.obj_var:", dc2.obj_var
dc1.obj_var = "new_object_data"
print "AFTER"
print "dc1.obj_var: ", dc1.obj_var
print "dc2.obj_var:", dc2.obj_var
# print

# print "i is class data member:"
# print "BEFORE:"
# print "m1.i: ", m1.i
# print "m2.i:", m2.i
# MyClass.class_data = ""
# m1.i = -1
# print "AFTER"
# print "m1.i: ", m1.i
# print "m2.i:", m2.i
