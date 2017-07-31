import collections

print(dir(collections))

print(239*'-')
from collections import namedtuple
help(namedtuple)

color = (55, 155, 255)
print(color[0])


dict_color = {'red' : 55, 'green' : 155, 'blue' : 255}
print(dict_color['red'])

#namedtuple
named_color = namedtuple('NamedColor', ['red', 'green', 'blue'])
named_color_tuple_type1 = named_color(255, 100, 155)
named_color_tuple_type2 = named_color(255, 155, blue=200)

print(named_color_tuple_type1)
print(named_color_tuple_type2)
print(named_color_tuple_type1[0])
print(named_color_tuple_type2.green)

#namedtuple to dictionary
dict_named_tuple = named_color_tuple_type2._asdict()
# dict_named_tuple['yellow'] = 225
print(dict_named_tuple)

#dictionary to namedtuple
namedtuple_from_dictionary = named_color(**dict_named_tuple)
print(namedtuple_from_dictionary)
print(type(namedtuple_from_dictionary))

#replace value
named_color_tuple_type3 = named_color_tuple_type2._replace(green = 225)
print(named_color_tuple_type3)

print(239*'-')
from collections import deque
help(deque)
# 5 - maxlen is optional
queue = deque(['Apple', 'Banana', 'Grapes', 'Orange'],10) 
print(queue)
print(queue.maxlen)
#append
queue.append('Strawberry')
print(queue)
queue.appendleft('Guava')
print(queue)
# rotate
queue.rotate()
print(queue)
queue.rotate(2)
print(queue)
queue.rotate(-3)
print(queue)
# pop
item = queue.pop()
print(item)
print(queue)

itemleft = queue.popleft()
print(itemleft)
print(queue)

# remove and reverse
queue.reverse()
print(queue)
queue.remove('Apple')
print(queue)

#Dunder Methods
queue.__setitem__(0, 'Apple')
print(queue)

#extend
queue.extend(['Anjeer', 'Pineapple'])
print(queue)

queue.extendleft(['Watermellon', 'Muskmellon'])
print(queue)

print(239*'-')
from collections import defaultdict
help(defaultdict)

