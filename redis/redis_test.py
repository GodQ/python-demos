import redis
import sys

def _tests():
    print('redis://172.29.16.71:6387/0')
    pool = redis.ConnectionPool.from_url("redis://172.29.16.71:6387/0")
    print(pool)
    r = redis.Redis(connection_pool=pool)
    print(r)
    r.set('one', 'first')
    r.set('two', 'second')
    print(r.get('one'))
    print(r.get('two'))

def _test_from(url):
    print(url)
    pool = redis.ConnectionPool.from_url(url)
    print(pool)
    r = redis.Redis(connection_pool=pool)
    print(r)
    r.set('one', 'first')
    r.set('two', 'second')
    print(r.get('one'))
    print(r.get('two'))

argv = sys.argv
l = len(argv)
if l==1:
    _tests()
else:
    url = argv[1]
    _test_from(url)
