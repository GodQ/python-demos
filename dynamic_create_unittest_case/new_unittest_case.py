
import unittest
import random


# def add_test_method(cls):
#     def wrap(self):
#         print(1,2,3,4)
#         assert random.randint(0, 1) == random.randint(0, 1)
#     setattr(cls, 'test1', wrap)
#     setattr(cls, 'test2', wrap)
#     return cls
#
# @add_test_method
# class T(unittest.TestCase):
#     pass

def feed_data(data):
    def test_method(self):
        print(data)
        assert random.randint(0, 1) == random.randint(0, 1)
    return test_method


def build_test():
    for d in ['dir1', 'dir2']:
        class_name = "Test" + d
        new_class = type(class_name, (unittest.TestCase,), {})
        print(new_class)
        test_method_count = 0
        for f in ['f1', 'f2']:
            test_name = "test_" + f
            setattr(new_class, test_name, feed_data(test_name))
            test_method_count += 1
        print(dir(new_class))
        if test_method_count > 0:
            globals()[class_name] = new_class

build_test()


class TestT(unittest.TestCase):
    pass

# import pytest

# @pytest.mark.p0
# def test_aaa():
#     print('mark.p0')
#     assert 1==0

# class ValidateFailure(AssertionError):
#     pass
#
# class TTT(unittest.TestCase):
#     def test_error(self):
#         raise ValidateFailure('aaa')
