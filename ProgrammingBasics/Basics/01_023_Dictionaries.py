#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

gradeDict = {'Rajeev':89, 'Gireesha':82, 'Dewakar':94, 'Malasani':97}
print(gradeDict)
print(len(gradeDict))

print(gradeDict['Gireesha'])

gradeDict['Gireesha'] = 28;
print(gradeDict)

del(gradeDict['Gireesha'])
print(gradeDict)

print(len(gradeDict))

gradeDict = {'Rajeev':[89, 92], 
			 'Dewakar':[94, 97],
			 'Malasani':[97, 95]}
			 
print(gradeDict)
print(len(gradeDict))

print(gradeDict['Malasani'][1])
print(gradeDict['Dewakar'][0])


keyList = list(gradeDict.keys())
print(keyList)
print(sorted(keyList))

squareDict = {x: x**2 for x in (2,4,6)}
print(squareDict)


#Looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for i,v in knights.items():
	print(i,v)
	
for i,v in enumerate(['tic', 'tac', 'toe']):
	print(i,v)
	
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot' , 'the holy grail', 'blue']
for q,a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q,a))

