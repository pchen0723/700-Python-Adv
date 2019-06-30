# Collect several exception and process the error all the same way.
try:
   print(x)
except (NameError, SyntaxError) as msg:
    print("Variable x is not defined", msg)