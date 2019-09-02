import fire
class Test(object):

    def __init__(self):
        self.s = "init"

    def set(self, s):
        self.s = s
        return self

    def show(self):
        print(self.s)
        return self


if __name__ == '__main__':
  fire.Fire(Test)