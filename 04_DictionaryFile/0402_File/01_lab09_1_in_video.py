#!/usr/bin/env python
"""lab09_1_from_video.py Dictionary implementation for demonstrating
   a dictionary.
   This is the version of the lab exercise that is shown in the video.
   An improved version is lab09_01.py
"""
from py_dict_in_video import *  # Careful of this!
def ListDefinitions():
    """Prints out the dictionary, alphabetically by the meanings"""
    defs = []     # or:  defs = [(v, k) for (k, v) in py_dict.items()]
    for k, v in py_dict.items(): 
        defs += [(v, k)]         
    defs.sort()
    for (v, k) in defs:
        print (v, ':', k)

'''
def ListDefinitions():
    """Prints out the dictionary, alphabetically by the meanings --
implemented via a sort function."""
    def ValueKey(x):
        return py_dict[x]
    for each in sorted(py_dict, key=ValueKey):
        print (py_dict[each], ':', each)
'''

def main():
    """Runs the user interface for dictionary manipulation."""
    choices = {'add': CollectEntries, 'definitions': ListDefinitions,
               'find': FindDefinitions, 'print': PrintEntries}
    prompt = MakePrompt(choices)
    while True:
        raw_choice = input(prompt)
        if not raw_choice:
            break
        given_choice = raw_choice[0].lower()
        for maybe_choice in choices:
            if maybe_choice[0] == given_choice:
                choices[maybe_choice]()
                break
        else:
            print ('%s is not an acceptible choice.' % raw_choice)
if __name__ == '__main__':
    main()
"""
$ lab09_1_from_video.py
Choose (a)dd, (d)efinitions, (f)ind, (p)rint (enter to quit) d
an object used to access a value in a dictionary : key
break out of a loop and skip the else : break
do nothing : pass
go to the next iteration of the loop : continue
Choose (a)dd, (d)efinitions, (f)ind, (p)rint (enter to quit) 
$"""