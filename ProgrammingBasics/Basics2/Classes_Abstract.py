from abc import ABCMeta, abstractmethod

class BaseClass(object):
    """docstring for BaseClass."""
    __metaclass__  = ABCMeta
    @abstractmethod
    def printHam(self):
        pass


class InClass(BaseClass):
    """docstring for InClass."""
    def printHam(self):
        print 'ham'



x = InClass()
x.printHam()
