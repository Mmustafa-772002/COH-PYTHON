my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
    
}
print(" my name is ",my_dict["name"])
print(" my age is ",my_dict["age"])
print(" my city is ",my_dict["city"])


# input in the dictionry 
new_dict = {}
a = input("enter the name : ")
b = input("enter the age : ")
c = input("enter the city : ")
new_dict["name"] = a
new_dict["age"] = b
new_dict["city"] = c
print(new_dict)



# dictionary and set - the dictionary is a data type in python that is used to store key-value pairs. A set is a collection of unique elements.
# |-------|------------|------------------------|
# | index | function   |     example            |
# |-------|------------|------------------------|
# | 1     | clear      | example.clear()        |
# | 2     | copy       | example.copy()         |
# | 3     | fromkeys   | example.fromkeys()     |
# | 4     | get        | example.get()          |
# | 5     | items      | example.items()        |
# | 6     | keys       | example.keys()         |
# | 7     | pop        | example.pop()          |
# | 8     | popitem    | example.popitem()      |
# | 9     | setdefault | example.setdefault()   |
# | 10    | update     | example.update()       |
# | 11    | values     | example.values()       |
# |-------|------------|------------------------|

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

# set - the set is a collection of unique elements and it is unordered and un-indexed and the set is also mutable and the set is written with curly brackets.

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

# set -  it is the collection of unique elements and it is unordered and un-indexed and it is mutable and it is written with curly brackets. and the set is also used to perform the mathematical operations like union, intersection, difference, symmetric difference, etc.
# the set methods

# |-------|------------------------------|-----------------------------------------------|
# | index | function                     |     example                                   |
# |-------|------------------------------|-----------------------------------------------|
# | 1     | add                          | example.add("orange")                         |
# | 2     | clear                        | example.clear()                               |
# | 3     | copy                         | example.copy()                                |
# | 4     | difference                   | example.difference()                          |
# | 5     | difference_update            | example.difference_update()                   |
# | 6     | discard                      | example.discard("apple")                      |
# | 7     | intersection                 | example.intersection()                        |
# | 8     | intersection_update          | example.intersection_update()                |
# | 9     | isdisjoint                   |  example.isdisjoint()                          |
# | 10    | issubset                     | example.issubset()                            |
# | 11    | issuperset                   | example.issuperset()                          |
# | 12    | pop                          | example.pop()                                 |
# | 13    | remove                       | example.remove("apple")                       |
# | 14    | symmetric_difference         | example.symmetric_difference()              |
# | 15    | symmetric_difference_update  | example.symmetric_difference_update()|
# | 16    | union                        | example.union()                               |
# | 17    | update                       | example.update()                              |
# |-------|-----------------------------|-----------------------------------------------|


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
print(example.symmetric_difference(example1))

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
example.update(example1)
print(example)

# you cannot add list in to the set because the list is mutable and the set is immutable and the set is also used to perform the mathematical operations like union, intersection, difference, symmetric difference, etc.
# we can not add dictionary in to the set because the dictionary is mutable and the set is immutable and the set is also used to perform the mathematical operations like union, intersection, difference, symmetric difference, etc.
