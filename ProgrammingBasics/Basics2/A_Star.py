try:
    from Queue import PriorityQueue
except:
    from queue import PriorityQueue

import pdb

class State(object):
    """docstring for State."""
    def __init__(self, value, parent, start = 0, goal = 0):
        #pdb.set_trace()
        super(State, self).__init__()
        self.children = []
        self.parent = parent
        self.value = value
        self.distance = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def getDistance(self):
        pass

    def createChildren(self):
        pass

class State_String(State):
    """docstring for State_String."""
    def __init__(self, value, parent, start = 0, goal = 0):
        super(State_String, self).__init__(value, parent, start, goal)
        self.distance = self.getDistance()

    def getDistance(self):
        #pdb.set_trace()
        if self.value == self.goal:
            return 0
        else:
            distance = 0
            for i in range(len(self.goal)):
                letter = self.goal[i]
                distance += abs(i - self.value.index(letter))
            return distance

    def createChildren(self):
        #pdb.set_trace()
        if not self.children:
            for i in range(len(self.goal) - 1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_String(val, self)
                self.children.append(child)

class AStarSolver(object):
    """docstring for AStarSolver."""
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def solve(self):
        startState = State_String(self.start, 0, self.start, self.goal)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            print(self.priorityQueue)
            closetChild = self.priorityQueue.get()[2]
            closetChild.createChildren()
            self.visitedQueue.append(closetChild.value)
            for child in closetChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.distance:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.distance, count, child))
        if(not self.path):
            print('Goal of '+ self.goal + 'is not possible!')
        return self.path

##============================================MAIN============================================
if __name__ == '__main__':
    start1 = 'cba'
    goal1 = 'abc'
    print('Starting...')
    a = AStarSolver(start1, goal1)
    a.solve()
    for i in range(len(a.path)):
        print("%d) "%i + a.path[i])
