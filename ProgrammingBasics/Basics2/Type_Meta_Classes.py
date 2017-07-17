class MyClass(object):
    """docstring for MyClass."""
    pass

print dir()
x = MyClass()
print MyClass
print x
print type(x)
print MyClass == type(x)
print type(MyClass)

class NewClass(object):
    """docstring for NewClass."""
    def __init__(self):
        super(NewClass, self).__init__()
        self.x = 5

#add later
def printHam(self):
    print 'ham'

TypeClass = type("TypeClass",(object,),{'x':5, 'pH':printHam})
n = NewClass()
t = TypeClass()
print n.x,t.x
t.pH()


print type('1')
print type(type('1'))

print '1'.__class__
print '1'.__class__.__class__


class Singleton(type):
    """docstring for Singleton."""
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            cls.x = 5
        return cls._instances[cls]

class SngClass(object):
    __metaclass__ = Singleton

m = SngClass()
s = SngClass()
print m.x
s.x = 11
print s.x
