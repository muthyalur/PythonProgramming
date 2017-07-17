#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

try:
	name = str(input('Enter you name: '))
	print('Hello',name)
	
	x = input('Enter x value: ')
	y = input('Enter y value: ')
	result = (int(x) / int(y))
	
except ZeroDivisionError as _z:
	print('Divide by zero error.')
	print(str(_z))
except TypeError as _t:
	print('Type Error triggered')
	print(str(_t))
except Exception as _e:
	print(str(_e))
else:
	print('No Runtime Error triggered')	
finally:
	print('executing finally clause')
	
try: 
	raise Exception('spam','eggs')
except Exception as e:
	x, y = e.args
	print(x)
	print(y)
finally:
	print('finally block executed')