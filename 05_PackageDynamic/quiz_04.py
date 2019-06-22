class Person:
  name = "John"
  age = 36
  country = "Norway"

# Note the 'age1" is the namespace is existed.
setattr(Person, 'age', 40)
print (Person.age)

# Note the 'age1" is the namespace will be existed.
setattr(Person, 'age1', 20)
print (Person.age1)