# list and tuples
# the list are containers that can hold a number of other objects.
# this is oredered and changeable
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(example)
# the indexing in the list starts from 0

print(example[0])
print(example[1])
print(example[2])
print(example[3])

# to print the strings in the list
example = ["apple", "banana", "cherry"]
print(example)
print(example[0])
print(example[1])
print(example[2])
example[1] = "blackcurrant"
print(example)

# we can print the different data types in the list
# |-------|------------|----------------------------|
# | index | function   |     example                |
# |-------|------------|----------------------------|
# | 1     | append     | example.append(11)         |
# | 2     | clear      | example.clear()            |
# | 3     | copy       | example.copy()             |
# | 4     | count      | example.count(5)           |
# | 5     | extend     | example.extend(example1)   |
# | 6     | index      | example.index(7)           |
# | 7     | insert     | example.insert(1, 12)      |
# | 8     | pop        | example.pop()              |
# | 9     | remove     | example.remove(5)          |
# | 10    | reverse    | example.reverse()          |
# | 11    | sort       | example.sort()             |
# | 12    | sort       | example.sort(reverse=True) |
# | 13    | sort       | example.sort(reverse=False)|
# |-------|------------|----------------------------|

example = ["apple", "banana", "cherry", 1, 2, 3]
print(example)

# list slicing
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(example[2:5])
print(example[:5])
print(example[5:])
print(example[-5:-2])

# to change the value of the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example[1:3] = [13, 14]
print(example)

# to insert the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example.insert(1, 12)
print(example)

# to append the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example.append(11)
print(example)

# to remove the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example.remove(5)
print(example)

# to pop the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example.pop()
print(example)

# to clear the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example.clear()
print(example)

# to copy the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example1 = example.copy()
print(example1)

# to count the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = example.count(5)
print(x)

# to extend the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example1 = [11, 12, 13, 14, 15]
example.extend(example1)
print(example)

# to index the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = example.index(7)
print(x)

# to reverse the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example.reverse()
print(example)

# to sort the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example.sort()
print(example)

# to sort the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example.sort(reverse=True)
print(example)

# to sort the value in the list
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example.sort(reverse=False)
print(example)

# append()  -	Adds an element at the end of the list
# clear()   -	Removes all the elements from the list
# copy()    -	Returns a copy of the list
# count()   -	Returns the number of elements with the specified value
# extend()  -	Add the elements of a list (or any iterable), to the end of the current list
# index()   -	Returns the index of the first element with the specified value
# insert()  -	Adds an element at the specified position
# pop()     -	Removes the element at the specified position
# remove()  - Removes the first item with the specified value
# reverse() -	Reverses the order of the list
# sort()    -	Sorts the list

example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(example)
b = int(input("Enter the number to be added in the list: "))
example.append(b)
print(example)

example = ["apple", "banana", "cherry"]
print(example)
b = input("Enter the string to be added in the list: ")
example.append(b)
print(example)

f1  = input("enter the fruit name f1 : ")
f2  = input("enter the fruit name f2 : ")
f3 = input("enter the fruit name f3 : ")
f4 = input("enter the fruit name f4 : ")
f5  = input("enter the fruit name f5 : ")
f6  = input("enter the fruit name f6 : ")
f7  = input("enter the fruit name f7 : ")
f8  = input("enter the fruit name f8 : ")
f9  = input("enter the fruit name f9 : ")

myLIST = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
print(myLIST)
