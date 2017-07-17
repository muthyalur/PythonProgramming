#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
appendText = 'This is a more text'

saveFile = open('.\01_014_016_FileOperations\FileExample.txt', 'a')
saveFile.write('\n'*30)
saveFile.write(appendText)
saveFile.close()
