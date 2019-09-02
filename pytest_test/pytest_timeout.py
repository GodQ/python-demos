
# coding: utf-8
import unittest
import time
import pytest


class BTest(unittest.TestCase):
    def setUp(self):
        print("Test case started")

    @pytest.mark.timeout(timeout=6)
    def test_b1(self):
        time.sleep(5)
        pass

    def test_b2(self):
        pass

    def tearDown(self):
        print("Test case finished")


if __name__ == '__main__':
    unittest.main()
