# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    def testRightTriangle(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testEquilateral(self):
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral')

    def testIsoceles(self):
        self.assertEqual(classifyTriangle(5,5,3),'Isoceles')

    def testScalene(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle')

    def testInvalidNegative(self):
        self.assertEqual(classifyTriangle(-1,2,3),'InvalidInput')

    def testInvalidZero(self):
        self.assertEqual(classifyTriangle(0,2,3),'InvalidInput')

    def testInvalidLarge(self):
        self.assertEqual(classifyTriangle(201,2,3),'InvalidInput')

    def testInvalidType(self):
        self.assertEqual(classifyTriangle(2.5,3,4),'InvalidInput')

if __name__ == '__main__':
    unittest.main()
