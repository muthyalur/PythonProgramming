class Ph:
    def __init__(self):
        self.y = 5
        z = 10
        self.printHam()
    def printHam(self):
        print 'ham'

x = Ph()
#x.printHam()
print x.y
'''
AttributeError: Ph instance has no attribute 'z'
print x.z
'''




class Hero:
    """A hero is allergetic to apple"""
    def __init__(self, name):
        self.name = name
        self.health = 100
    def eat(self,food):
        """A hero eats whatever food you feed.."""
        if(food == 'apple'):
            self.health -= 100
        elif(food == 'ham'):
            self.health += 20

if __name__ == '__main__':
    Bob = Hero('Bob')
    print Bob.name
    print Bob.eat.__doc__
    Bob.eat('apple')
    print Bob.health
    print Bob.__doc__
    Bob.eat('ham')
    print Bob.health



class AddFive():
    """adds 5 to given value"""
    def add(self, var):
        return (var + 5)

class Num():
    def __init__(self, value):
        self.val = value
        self.otherVal = None

n = Num(value = 25)
a5 = AddFive()
n.otherVal = a5.add(n.val)
print n.val, n.otherVal
