#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
condition = 1

while condition < 10:
	print(condition)
	condition += 1

print('End While Loop')


a,b = 0,1
while b < 10:
	print(b)
	a,b = b, a+b
	
	
a,b = 0,1
while b < 1000:
	print(b, end=",")
	a,b = b, a+b

print()

for i in range(0, 10, 3):
	print(i)
	
	
a = list(range(0,10,2))
for i in a:
	print(i)
	
b = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(b)):
	print(i, b[i])
	
