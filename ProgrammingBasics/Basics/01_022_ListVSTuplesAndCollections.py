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


#List as Queues

from collections import deque

queue = deque(["Apple", "Banana", "Grapes", "Mango", "Orange"])
print(queue)
queue.pop()
print(queue)
queue.append("Strawberry")
print(queue)
queue.popleft()
print(queue)

#List Comprehensions

squares = []
for x in range(0,10):
	squares.append(x**2)
print(squares)

squares = [x**2 for x in range(0,10)]
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

listOfList = [(x, y) for x in [1,2,3] for y in [3,1,4] if x!= y]
print(listOfList)


vec = [-4, -2, 0, 2, 4]
print([x**2 for x in vec])


fruits = [' banana     ', 'loganberry    ', 'passion fruit     ', 'apple fruit'];
fresh_fruits = [weapon.strip() for weapon in fruits]
print(fresh_fruits)

#Nested List Comprehensions

matrix = [
			[1,2,3,4],
			[5,6,7,8],
			[9,10,11,12],
		]
		
print(matrix)

transformed_matrix = [[(row[i]) for row in matrix] for i in range(4)]
print(transformed_matrix)

transformed_matrix_1 = list(zip(*matrix))
print(transformed_matrix_1)


#sets

basket = ['apple' , 'banana', 'apple', 'mango', 'oranges', 'grapes', 'pear', 'oranges', 'banana']
print(basket)
basket_set = set(basket)
print(basket_set)


basket_set1 = {'apple' , 'banana', 'apple', 'mango', 'oranges', 'grapes', 'pear', 'oranges', 'banana'}
print(basket_set1)

#set comprehensions
set_comp = {x for x in 'abracadabra'}
print(set_comp)

set_comp = {x for x in 'abracadabra' if x not in 'abc'}
print(set_comp)
