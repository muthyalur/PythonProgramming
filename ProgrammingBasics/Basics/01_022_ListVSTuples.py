#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
def example():
	return 15, 19
	
a, b = example()
print(a)
print(b)

x = [6,2,3,6,6,8,4,9,3]
print(x)

x.append(12)
print(x)

print(x[5])

x.insert(5,7)
print(x)

print(len(x))

print(x.count(6))

print(x.index(2))

x.remove(6)
print(x)

x.sort()
print(x)

x.reverse()
print(x)

y = ['Sachin', 'Tendulkar', 'Gangully', 'Ashwin', 'Zaheer Khan']
y.reverse()
print(y)

y.sort()
print(y)

y.reverse()
print(y)

squares = [1,4,9,16,25]
print(squares)


x.extend(y)
x.extend(squares)
print(x)
x.pop(10)
print(x)


L = range(1,100)
k = list(filter(lambda x: x%2 == 0, L))
print(k)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six')]
pairs.sort(key = lambda pair: pair[1], reverse = True)
print(pairs)


a = (1,2,3)
b = (4,5)

a += b
print(a)

c = [2,3,4,5]
d = [6,7,8,10,2,3]
e = c + d
print(e)
e.append(10)
print(e)
t = ['test']
print(t)
print(list('test'))


import sys
list_ex = [1, 2, 3, 'a', 'b', 'c', True, 3.14159]
tuple_ex = (1, 2, 3, 'a', 'b', 'c', True, 3.14159)

print("List size = ",sys.getsizeof(list_ex))
print("Tuple size = ",sys.getsizeof(tuple_ex))


import timeit
list_test = timeit.timeit(stmt = "[1, 2, 3, 4, 5]", number = 1000000)
tuple_test = timeit.timeit(stmt = "(1, 2, 3, 4, 5)", number = 1000000)
print("List time: ", list_test)
print("Tuple time: ", tuple_test)
