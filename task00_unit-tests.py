##
## EPITECH PROJECT, 2026
## day02
## File description:
## task00_unit-tests
##

import unittest as test
from task00 import multiply
from task00 import multiply10
from task00 import multiply2
from task00 import getSecondMax

class TestMultiply ( test.TestCase ) :
    def test_multiply_integers ( self ) :
        self.assertEqual ( multiply (3 , 4) , 12)

    def test_multiply_floats ( self ) :
        self.assertAlmostEqual ( multiply (1.5 , 2) , 3.0)

class TestMutiply2 (test.TestCase):
    def test_multiply2_int(self):
        self.assertEqual(multiply2(2), 4)
    
    def test_multiply2_float(self):
        self.assertAlmostEqual(multiply2(1.5), 3.0)

class TestMutiply10(test.TestCase):
    def test_multiply10_int(self):
        self.assertEqual(multiply2(2), 20)
    
    def test_multiply2_float(self):
        self.assertAlmostEqual(multiply2(1.5), 15.0)

class TestGetSecondMax(test.TestCase):
    def test_getSecondMax_simple_int(self):
        self.assertEqual(getSecondMax([1, 2, 3]), 2)
    
    def test_getSecondMax_multiple_same_int(self):
        self.assertEqual(getSecondMax([5, 5, 2]), 2)

    def test_getSecondMax_all_same_int(self):
        self.assertEqual(getSecondMax([5, 5, 5]), 5)


    def test_getSecondMax_simple_float(self):
        self.assertEqual(getSecondMax([1.5, 2.5, 3.5]), 2.5)
    
    def test_getSecondMax_multiple_same_float(self):
        self.assertEqual(getSecondMax([5.5, 5.5, 2.5]), 2.5)

    def test_getSecondMax_all_same_float(self):
        self.assertEqual(getSecondMax([5.4, 5.4, 5.4]), 5.4)


if __name__ == " __main__ " :
    test.main()
