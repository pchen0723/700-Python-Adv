#!/usr/bin/env python
"""The argument you give to your raise can be anything, a string is
most common, but a tuple is possible."""
     
def GetPositiveNumber(prompt):
    said = input(prompt)
    #print('said: ', said)
    number = float(said)
    print ('number:', number)
    if number < 0:
        raise ValueError ("Number given must be positive.", number)
    return number
try:
    number = GetPositiveNumber("Positive number please: ")
except ValueError as msg:
    # print ("msg[0] =", msg[0])
    # print ("msg[1] =", msg[1])
    print ('msg:', msg)

"""
$ raise3.py
Positive number please: -1
msg[0] = Number given must be positive.
msg[1] = -1.0
$ """