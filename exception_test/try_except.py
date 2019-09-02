

try:
    raise Exception("123456")
except Exception as e:
    print(e)
    print(dir(e))
    print(type(e))
    print(str(e))
    print("")


class Exp(Exception):
    def __init__(self, msg=None):
        self.msg = msg

try:
    raise Exp("123456")
except Exception as e:
    print(e)
    print(dir(e))
    print(type(e))
    print(str(e))
