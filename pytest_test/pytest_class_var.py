
# coding: utf-8
import unittest
import time
import pytest

var = 0

class BTest(unittest.TestCase):
    def setUp(self):
        print("Test case started")

    def test_b1(self):
        global var
        print(var)
        var = 1
        assert 0

    def test_b2(self):
        global var
        print(var)
        var = 2
        assert 0

    def tearDown(self):
        print("Test case finished")


if __name__ == '__main__':
    unittest.main()
