help(set)
example_1 = set()
example_1.add(42)
example_1.add(False)
example_1.add(3.14159)
example_1.add("Thorium")
print(example_1)
print(len(example_1))

example_1.add(42)
print(example_1)
print(len(example_1))

example_1.add(48)
print(example_1)
print(len(example_1))

example_1.remove(48)
print(example_1)
print(len(example_1))

example_1.discard(48) #remove will throw error
print(example_1)
print(len(example_1))

example_2 = set([28, True, 2.71828, "Helium"])
print(example_2)
print(len(example_2))

example_2.clear()
print(example_2)
print(len(example_2))


evens = set([0, 2, 4, 6, 8, 10])
odds = set([1, 3, 5, 7, 9])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9])

print("evens: ", evens)
print("odds: ", odds)
print("primes: ", primes)
print("composites: ", composites)


print(odds.union(evens))
print(evens.intersection(composites))
print(odds.intersection(primes))
print(evens.intersection(odds))
print(evens.intersection(primes))


print(2 in primes)
print(1 not in composites)