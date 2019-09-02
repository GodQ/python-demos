
class Singleton(type):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        print "Singleton new"
        return super(Singleton, cls).__new__(cls, *args, **kwargs)

    def __init__(cls, classname, parrentstuple, attrdict):
        print "Singleton init"
        super(Singleton, cls).__init__(classname, parrentstuple, attrdict)

    def __call__(cls, *args):
        print "Singleton call start"
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args)
            print "Singleton call end"
        print cls._instances
        return cls._instances[cls]

class Test(object):
    __metaclass__ = Singleton
    def __new__(cls, *args, **kwargs):
        print "Test new"
        return super(Test, cls).__new__(cls, *args, **kwargs)
    def __init__(self):
        print "Test init"

class Test1(object):
    def __new__(cls, *args, **kwargs):
        print "Test1 new"
        return super(Test1, cls).__new__(cls, *args, **kwargs)
    __metaclass__ = Singleton
    def __init__(self):
        print "Test init"

t=Test()
print id(t)
t1=Test1()
print id(t1)
t1=Test1()
print id(t1)
