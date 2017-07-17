BaseClass = type("BaseClass",(object,),{})

#add later
@classmethod
def Check1(self, myStr):
    return myStr == 'ham'

@classmethod
def Check2(self, myStr):
    return myStr == 'sandwich'

C1 = type("C1",(BaseClass,),{'x':1, 'Check':Check1})
C2 = type("C2",(BaseClass,),{'x':30, 'Check':Check2})

def MyFactory(myBool):
    return C1() if myBool else C2()

m = MyFactory(True)
v = MyFactory(False)
print m.x, v.x


def NewFactory(myStr):
    for cls in BaseClass.__subclasses__():
        if cls.Check(myStr):
            return cls()


a = NewFactory('ham')
b = NewFactory('sandwich')
print a.x, b.x
