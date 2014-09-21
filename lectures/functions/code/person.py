def display(name, age, sex="M"):
   print "Name: ", name
   print "Age: ", age
   print "Sex: ", sex

display("Lary", 43, "M")
display("Lary", age=43)
display("Lary", age=43, sex="M")
display(age=43, name="Lary", sex="M")
