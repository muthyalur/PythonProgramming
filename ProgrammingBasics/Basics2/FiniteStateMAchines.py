'''
Finite = limited number

State = How something is in that moment(Cold, Gas, ...)

Machine = you know what it is.. :)

'''
from random import randint
from time import clock

##==============================================================
State = type('State',(object,), {})

class LightOn(State):
    """docstring for LightOn."""
    def execute(self):
        print('Light is On!')

class LightOff(State):
    """docstring for LightOff."""
    def execute(self):
        print('Light is Off!')
##==============================================================
class Transistion(object):
    """docstring for Transistion."""
    def __init__(self, toState):
        super(Transistion, self).__init__()
        self.toState = toState

    def execute(self):
        print('Transitioning...')
##==============================================================
class FSM(object):
    """docstring for FSM."""
    def __init__(self, char):
        super(FSM, self).__init__()
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None

    def setState(self, stateName):
        self.curState = self.states[stateName]

    def transition(self, transName):
        self.trans = self.transitions[transName]

    def execute(self):
        if(self.trans):
            self.trans.execute()
            self.setState(self.trans.toState)
            self.trans = None
        self.curState.execute()
##==============================================================
class Char(object):
    """docstring for char."""
    def __init__(self):
        super(Char, self).__init__()
        self.simpleFSM = FSM(self)
        self.isLightOn = True
##==============================================================

if __name__ == '__main__':
    light = Char()

    light.simpleFSM.states['On']=LightOn()
    light.simpleFSM.states['Off']=LightOff()
    light.simpleFSM.transitions['toOn']=Transistion('On')
    light.simpleFSM.transitions['toOff']=Transistion('Off')

    light.simpleFSM.setState('On')

    for i in range(20):
        startTime = clock()
        timeInterval = 1
        while(startTime+timeInterval>clock()):
            pass
        rInt =  randint(0,2)
        print('rInt: %d'%rInt)
        if(rInt):
            if(light.isLightOn):
                light.simpleFSM.transition('toOff')
                light.isLightOn = False
            else:
                light.simpleFSM.transition('toOn')
                light.isLightOn = True
        light.simpleFSM.execute()
