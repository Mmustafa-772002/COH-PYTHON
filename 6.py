# dictionary and set - the dictionary is a data type in python that is used to store key-value pairs. A set is a collection of unique elements.
# clear()
# copy()
# fromkeys()
# get()
# items()
# keys()
# pop()
# popitem()
# setdefault()
# update()
# values()

# clear() - 	Removes all the elements from the dictionary
example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example.clear()
print(example)

# copy() - 	Returns a copy of the dictionary
example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example1 = example.copy()
print(example1)

# fromkeys() - 	Returns a dictionary with the specified keys and value
example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example1 = example.fromkeys(["brand", "model"], "default_value")
print(example1)


# get() - 	Returns the value of the specified key

example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example1 = example.get("brand")
print(example1)


# items() - 	Returns a list containing a tuple for each key value pair

example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example1 = example.items()
print(example1)


# keys() - 	Returns a list containing the dictionary's keys

example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example1 = example.keys()
print(example1)


# pop() - 	Removes the element with the specified key

example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example.pop("model")
print(example)


# popitem() - 	Removes the last inserted key-value pair

example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example.popitem()
print(example)


# setdefault() - 	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example1 = example.setdefault("model", "Bronco")
print(example1)

# update() - 	Updates the dictionary with the specified key-value pairs

example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example.update({"color": "red"})
print(example)


# values() - 	Returns a list of all the values in the dictionary
example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
example1 = example.keys()
print(example1)
example2 = example.values()
print(example2)


example = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(example)
print(example["brand"])
print(example["model"])
print(example["year"])
print(example.get("model"))
print(example.get("year"))
print(example.get("brand"))
print(example.keys())
print(example.values())

example = {"apple", "banana", "cherry"}
print(example)
print("banana" in example)
example.add("orange")
print(example)

# set - the set is a collection of unique elements and it is unordered and unindexed and the set is also mutable and the set is written with curly brackets.

example = {"apple", "banana", "cherry"}
print(example)
example.add("orange")
print(example)
example.update(["orange", "mango", "grapes"])
print(example)
example.remove("banana")
print(example)
example.discard("apple")
print(example)
example.pop()
print(example)
example.clear()
print(example)

# set -  it is the collection of unique elements and it is unordered and unindexed and it is mutable and it is written with curly brackets. and the set is also used to perform the mathematical operations like union, intersection, difference, symmetric difference, etc.
# the set methods

# add()
# clear()
# copy()
# difference()
# difference_update()
# discard()
# intersection()
# intersection_update()
# isdisjoint()
# issubset()
# issuperset()
# pop()
# remove()
# symmetric_difference()
# symmetric_difference_update()
# union()
# update()


# add()	-  Adds an element to the set
example = {"apple", "banana", "cherry"}
print(example)

example.add("orange")
print(example)
print(type(example))

# clear()	-  Removes all the elements from the set
example = {"apple", "banana", "cherry"}
print(type(example))
print(example)
example.clear()
print(example)
# copy()	-  Returns a copy of the set
example = {"apple", "banana", "cherry"}
print(example)
example1 = example.copy()
# difference()	-  Returns a set containing the difference between two or more sets
example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
print(example.difference(example1))
# difference_update()	-  Removes the items in this set that are also included in another, specified set
example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
example.difference_update(example1)
example1.difference_update(example)
print(example)
# discard()	-  Remove the specified item
example = {"apple", "banana", "cherry"}
print(example)
example.discard("apple")

# intersection()	-  Returns a set, that is the intersection of two or more sets
example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
print(example.intersection(example1))
# intersection_update()	-  Removes the items in this set that are not present in other, specified set(s)
example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
print(example.intersection_update(example1))
# isdisjoint()	-  Returns whether two sets have a intersection or not
example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
print(example.isdisjoint(example1))
# issubset()	-  Returns whether another set contains this set or not
example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
print(example.issubset(example1))
# issuperset()	-  Returns whether this set contains another set or not
example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
print(example.issuperset(example1))
# pop()	-  Removes an element from the set
example = {"apple", "banana", "cherry"}
print(example)
example.pop()
print(example)
# remove()	-  Removes the specified element
example = {"apple", "banana", "cherry"}
print(example)
example.remove("apple")
# symmetric_difference()	-  Returns a set with the symmetric differences of two sets
example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
print(example.symmetric_difference(example1))


# symmetric_difference_update()	-  inserts the symmetric differences from this set and another
example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
print(example.symmetric_difference_update(example1))
# union()	-  Return a set containing the union of sets

example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
print(example.union(example1))
# update()	-  Update the set with another set, or any other iterable

example = {"apple", "banana", "cherry"}
example1 = {"google", "microsoft", "apple"}
example.update(example1)  # TODO complete next  
print(example)





