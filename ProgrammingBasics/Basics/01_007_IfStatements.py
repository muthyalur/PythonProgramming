#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
x = 2
y = 7
z = 10

if x>y:
	print(x,'is greater than',y)
	
if x<y:
	print(x,'is lesser than',y)
	
if x==z:
	print(x,'same as',z)
	
if x<=y:
	print(x,'is less than or equal to',y)
	
'''	
if x<'2':
	print(x,' is less than 2')
'''

if z>y>x:
	print(z,'is greater than',y,'which is greater than',x)
