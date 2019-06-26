#!/usr/bin/env python
"""This example of unittest is taken from
http://www.python.org/doc/lib/module-unittest.html."""

import random
import unittest 

class TestSequenceFunctions(unittest.TestCase):
    
    def setUp(self):
        self.seq = range(10)

    def testShuffle(self):
        print()
        print ('testShuffle(self) => self:', self)
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(list(self.seq))
        #self.seq.sort()
        sorted (self.seq)
        self.assertEqual(self.seq, range(10))

    def testChoice(self):
        print()
        print ('testChoice(self) => self:', self)
        print ('self.seq:', self.seq)
        element = random.choice(self.seq)
        print ('element:', element)
        #self.assert_(element in self.seq)
        self.assertTrue (element in self.seq)

    def testSample(self):
        print()
        print ('testSample(self) => self:', self)
        self.assertRaises(ValueError, random.sample, self.seq, 20)
        for element in random.sample(self.seq, 5):
            #self.assert_(element in self.seq)
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    print ('unitest.main():')
    unittest.main()
"""
$ ./pyunit.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.006s

OK
$
"""
