#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

def example():
	x = 1
	y = 3
	print(x+y)

	if x < y:
		print(x,'is less than',y)

#def main():
example()



def fib(n):
	a,b = 0,1
	while (b < n):
		a,b = b,a+b
		print(a,end = ' ')
	print()

fib(100)
fib(1000)

def fib2(n):
	a,b = 0,1
	result = []
	while (b < n):
		a,b = b,a+b
		result.append(a)
	return result

f = fib2
print(f(2000))

f1 = fib2(100)
print(f1)

"""
def ask_ok(prompt, retries = 4, reminder = 'Please try again'):
	while True:
		ok = input(prompt)
		if ok.lower() in ['y', 'ye', 'yes']:
			return True
		elif ok.lower() in ['n', 'no', 'nope']:
			return False
		retries -= 1
		if retries <= 0:
			raise ValueError('invalid user response')
		print(reminder)

ask_ok('Do you want to quit?')
ask_ok('Are you sure want to overide? Press \'Yes\' or \'No\'... ', 2)
"""

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def concat(*args, sep="/"):
	return sep.join(args)

print(concat('earth', 'mars' , 'venus'))
print(concat('earth', 'mars' , 'venus', 'Jupiter', sep='.'))

def parrot(voltage, state='a stiff', action='voom'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.", end=' ')
	print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


def my_function():
	"""
	Do nothing, but document it.

    No, really, it doesn't do anything.
    """
	pass

print(my_function.__doc__)

def make_increment(n):
	return lambda x: x+n

k = make_increment(42)
print(k(0))
print(k(20))
print(k(1))

def add(a: int, b:int = 10) -> str:
	return str(a+b)

print('Add Annotations:', add.__annotations__)
print('Cheeseshop Annotations:', cheeseshop.__annotations__)
#print(add('a','b'))
print(add(10) +'k')
#print(add('k'+'m'))
