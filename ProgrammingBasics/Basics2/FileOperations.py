import time as t
from os import path

def createFile(dest):
    """
    The script creates a text file at the passed in location, names file based on date
    """

    date = t.localtime(t.time())
    name = '%d_%d_%d_%d_%d_%d.txt'%(date[0],date[1],date[2],date[3],date[4],date[5])
    if not(path.isfile(dest+name)):
        f = open(dest+name, 'w')
        f.write('\n'*30)
        f.close()


if __name__ == '__main__':
    createFile("/Users/rajeev/Documents/PythonProgramming/ProgrammingBasics/Basics2/")
    print 'done!!!'
