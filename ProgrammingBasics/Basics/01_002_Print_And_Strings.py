#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
print('Hello World')

print("Double Quotes")

print('concatena'+'tion')

print('I\'m 5')

print("I'm 5")

print('hello','there')

print('He said "hi"')


s = 'Hello, world.'
print(str(s))
print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200

s = 'The value of x is ' + repr(x) + ', and y is '+repr(y)+'...'
print(s)

hello = 'hello, world\n'
hellos = repr(hello)
print(hello)
print(hellos)

print(repr((x, y, ('spam', 'eggs'))))


for x in range(1, 11):
	print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
	print(repr(x*x*x).rjust(4))

for x in range(1, 11):
	print('{0:2d},{1:3d},{2:4d}'.format(x, x*x, x*x*x))
	
	
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))



print('We are the {} who say "{}!"'.format('Knights', 'Ni'))

print('We are the {1} who say "{0}!"'.format('Knights', 'Ni'))


print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

#'!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:


contents = 'eels'

print('My hovercraft is full of {}.'.format(contents))

print('My hovercraft is full of {!r}.'.format(contents))




