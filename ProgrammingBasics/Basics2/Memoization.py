
# one way
fibonacci_cache = {}

# other way - least recently used cache
# from functools import lru_cache

# @lru_cache(maxsize = 1000)
# def fibonacci(n):
# 	if type(n) != int:
# 		raise TypeError("n must be a positive int")
# 	elif n < 1:
# 		raise TypeError("n must be a positive int")
# 	elif n == 1:
# 		# print('fibonacci(',n,')')
# 		return 1
# 	elif n == 2:
# 		# print('fibonacci(',n,')')
# 		return 1
# 	elif n > 2:
# 		return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci(n):
	# If we have cached the value, then return it
	if(n in fibonacci_cache):
		return fibonacci_cache[n]
	
	# compute the Nth term
	if type(n) != int:
		raise TypeError("n must be a positive int")
	elif n < 1:
		raise TypeError("n must be a positive int")
	elif n == 1:
		# print('fibonacci(',n,')')
		value =  1
	elif n == 2:
		# print('fibonacci(',n,')')
		value = 1
	elif n > 2:
		value =  fibonacci(n - 1) + fibonacci(n - 2)

	# cache the value and return it	
	fibonacci_cache[n] = value  
	return value

# fibonacci(2.1)

for n in range(1, 11):
	print(n, ":", fibonacci(n))

for n in range(1, 101):
	print(n, ":", fibonacci(n))




import random

outcomes = ['rock', 'paper', 'scissors']

for i in range(20):
	print(random.choice(outcomes))