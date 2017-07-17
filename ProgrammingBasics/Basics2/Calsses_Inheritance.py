class BaseClass(object):
    """Base Class"""
    def printHam(self):
        print 'ham'

class InheritingClass(BaseClass):
    """Inheriting Class"""
    pass

ic = InheritingClass()
ic.printHam()

class BaseCharacter(object):
    def __init__(self, name):
        self.name = name
    def printName(self):
        print self.name

class NonPlayableCharacters(BaseCharacter):
    pass

class NPC_Friendly(NonPlayableCharacters):
    pass

class NPC_Enemy(NonPlayableCharacters):
    def __init__(self):
        self.attackDamage = 5


class PlayableCharacters(BaseCharacter):
    def __init__(self, name):
        super(PlayableCharacters, self).__init__(name)
        self.weapon = Weapon()

class Weapon():
    pass

class PC_Archer(PlayableCharacters):
    pass

class PC_Butcher(PlayableCharacters):
    pass

class PC_GreenLantern(PlayableCharacters):
    pass

pc = PlayableCharacters(name = 'Sachin')
pc.printName()


enemy = NPC_Enemy()
print enemy.attackDamage

butcher = PC_Butcher('Srinivasan')
butcher.printName()
print butcher.weapon
