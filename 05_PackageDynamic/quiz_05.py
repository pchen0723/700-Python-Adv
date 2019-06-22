def DoThis1():
        def Report():
            print (amount)
        amount = 3
        Report()

def DoThis2():
        def Report():
            print (amount)
        Report()
        amount = 3

print ('DoThis1:')
DoThis1()
print ('DoThis2:')
DoThis2()
