# which on is better
data = [1, 2, 3]
print ('for in:')
for datum in data: # better
    print (datum)

print ('\nindex:')
for index in range(len(data)):
    print (data[index])

# break
print ('\nindex < len():')
index = 0
while index < len(data):
    print (data[index]) 
    i += 1      # i is not defined