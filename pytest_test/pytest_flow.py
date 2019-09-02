
# coding: utf-8
import unittest
import time
import pytest
import pprint
from ddt import ddt, data, file_data, unpack

context = dict()
steps = [
    {"name": "test_1", "url": "test_1.com", 
     "input": {"a": 1, "b": 2}},
    {"name": "test_2", "url": "test_2.com", 
     "input": {"v1": "$test_1.response.body.b"}},
    {"name": "test_3", "url": "test_3.com", 
     "input": {"v2": "$test_2.response.header.h"}},
]

def do_reflect(input_t, context_t):
    input = input_t
    return input

def build_request(step):
    req = {"url": step["name"], "header": step["name"], "body": {"a": 1}}
    return req

def do_request(req):
    resp = {"header": {"h": 1}, "body": {"b": 1}}
    return resp

@ddt
class BTest(unittest.TestCase):
    def setUp(self):
        print("Test case started")

    @pytest.mark.timeout(2)
    @data(*steps)
    def test_step(self, step):
        global context
        print("Context: ", context)
        input = step["input"]
        print("Task: ", step)
        print("Input: ", input)
        input_ref = do_reflect(input, context)
        step["input"] = input_ref
        req = build_request(step)
        context[step["name"]] = dict()
        context[step["name"]]["request"] = req
        print("do request")
        resp = do_request(req)
        context[step["name"]]["response"] = resp
        assert 0

    def tearDown(self):
        print("Test case finished")

if __name__ == '__main__':
    unittest.main()
