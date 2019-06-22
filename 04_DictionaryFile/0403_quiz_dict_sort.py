name_dict= {}
name_dict['peter'] = 100
name_dict['jonathan'] = 90
name_dict['irene'] = 95
for name in sorted (name_dict): 
    print (name.capitalize(), ":", name_dict[name])

print ('name_dict: ', name_dict)

# Sorted by keys
import collections
name_dict1= {}
od_name_dict1= {}
name_dict1['peter'] = 100
name_dict1['jonathan'] = 90
name_dict1['irene'] = 95
od_name_dict1 = collections.OrderedDict(sorted (name_dict1.items()))

print ('od_name_dict1: ', od_name_dict1)
for name in od_name_dict1: 
    print (name.capitalize(), ":", od_name_dict1[name])