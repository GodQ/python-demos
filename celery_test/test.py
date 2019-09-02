#import sys
#sys.path.append(".")
from tasks import add
import time

def test():
    res = add.s(2, 2).delay()
    time.sleep(1)
    print(res.state)
    print(res.result)

test()
