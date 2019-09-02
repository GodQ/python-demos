
# coding: utf-8
import unittest
import time
import pytest
import pprint

context = dict()
steps = ["test_1","test_2","test_3"]

class BTest(unittest.TestCase):
    def setUp(self):
        print("Test case started")
    def tearDown(self):
        print("Test case finished")

@pytest.mark.timeout(2)
def template_method(self):
    pprint.pprint(context)
    t = time.time()
    context[t] = "aaa"
    print("done")
    assert 0

for step in steps:
    setattr(BTest, step, template_method)

if __name__ == '__main__':
    unittest.main()
