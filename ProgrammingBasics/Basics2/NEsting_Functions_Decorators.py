def outside(x = 5):
    def printHam():
        print 'ham'
        print x
    return printHam

myFunc = outside(100)
myFunc()


def addOne(myFunc):
    def addOneInside():
        return myFunc()+1
    return addOneInside

@addOne
def oldFunc():
    return 3

#Decorators
newFunc = addOne(oldFunc)
print oldFunc(), newFunc()


#oldFunc = addOne(oldFunc)
print oldFunc()


class MyClass:
    @classmethod
    def printHam(self):
        print 'ham'

MyClass.printHam()
