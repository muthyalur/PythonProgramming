#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

exampleList = [1,2,3,4,5,6,8,9,0,7]

for x in exampleList:
	print(x)
print('End For Loop')

for x in range(1,11):
	print(x)
	
	
for n in range(2,10):
	for m in range(2,n):
		if (n%m) == 0:
			print(n, 'equals', m,'*',n//m)
			break
	else:
		print(n, 'is a prime number')	
		
		
for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)		