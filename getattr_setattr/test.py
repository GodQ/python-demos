
class T:
    a = None
    def __init__(self):
        var_list = ['a', 'b', 'c']
        self.declare_vars(var_list)
        super().__setattr__("b", None)
        self.a = 1
        self.b = 1
        self.c = 1

    def declare_vars(self, var_list):
        for v in var_list:
            super().__setattr__(v, None)

    def __getattr__(self, attr):
        print("__getattr__", attr)
        if attr in dir(self):
            print("Old attr!", attr)
            super().__getattr__(attr)
        else:
            print("Unknown attr!")

    def __setattr__(self, attr, value):
        print("__setattr__", attr, value)
        if attr in dir(self):
            print("Old attr!", attr, value)
            super().__setattr__(attr, value)
        else:
            print("New attr!", attr, value)
            super().__setattr__(attr, value)


t = T()
print(t.a)
