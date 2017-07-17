#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
readMe = open('.\01_014_016_FileOperations\FileExample.txt', 'r').read()
print(readMe)
print(readMe.split())
print(readMe.split('\n'))

readMe2 = open('.\01_014_016_FileOperations\FileExample.txt', 'r').readline()
print(readMe2)

readMe3 = open('.\01_014_016_FileOperations\FileExample.txt', 'r').readlines()
print(readMe3)
