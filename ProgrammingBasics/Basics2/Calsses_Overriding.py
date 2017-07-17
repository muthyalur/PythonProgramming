class BaseClass(object):
    """docstring for BaseClass."""
    def __init__(self):
        self.x = 10

    def test(self):
        print 'ham'

class InClass(BaseClass):
    """docstring for InClass."""
    def __init__(self):
        super(InClass, self).__init__()
        self.x = 20

    def test(self):
        print 'hammer time'


ic = InClass()
print ic.x
ic.test()


print BaseClass.__subclasses__()
