# It is a good idea so that all calls to the function that do not 
# provide any arguments on the call will get the empty list as data.
def my_function(data = []):
#def my_function(data): # cause error when no parameter provide
    for x in data:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

fs = ["a", "b", "c"]
my_function(fs)

my_function() # error => for def my_function(food): # cause error when no parameter provide