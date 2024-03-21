#tuples - the tuples are containers that can hold a number of other objects.
# the tuple is also called as immutable list
# the tuples are ordered and unchangeable
# the tuple is written with the round brackets
# |-------|------------|----------------------------|
# | index | function   |     example                |
# |-------|------------|----------------------------|
# | 1     | count      | example.count(5)           |
# | 2     | index      | example.index(7)           |
# |-------|------------|----------------------------|

example = (1,2,3,4,5,6,7,8,9,10)
print(example)
# the indexing in the tuple starts from 0
print(example[0])
print(example[1])
print(example[2])
print(example[3])
# to print the strings in the tuple
example = ("apple", "banana", "cherry")
print(example)
print(example[0])
print(example[1])
print(example[2])
# we can print the diffrent data types in the tuple
example = ("apple", "banana", "cherry", 1, 2, 3)
print(example)
# tuple slicing
example = (1,2,3,4,5,6,7,8,9,10)
print(example[2:5])
print(example[:5])
print(example[5:])
print(example[-5:-2])
# the tuple have only two methods

# count()	Returns the number of times a specified value occurs in a tuple
example = (1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10)
print(example.count(5))
print(example.count(1))

# index()	Searches the tuple for a specified value and returns the position of where it was found
example = (1,2,3,4,5,6,7,8,9,10)
print(example.index(5))
print(example.index(1)) 