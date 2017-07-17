#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
x = 6
def example1():
	y = 7
	print(x)
	print(y)
def example2():
	z = 6
	z += 1
	y = x + 1
	#cannot do this
	#x += 1
	print(x)
	print(y)
	print(z)
	return y

def example3():
	z = 6
	z += 1
	y = 7
	x = example2()
	print(x)
	print(y)
	print(z)
	
def example4():
	global x
	z = 6
	z += 1
	y = 7
	x += 1
	print(x)
	print(y)
	print(z)	

example1()
example2()
example3()
example4()