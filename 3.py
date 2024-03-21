#  strings  - this is a data type in the python
#  example - "hello"

# the ' ' is also used in python as a string value
# example - 'hello'

# the """ """ is also used in python as a string value
# example - """hello"""

# the ''' ''' is also used in python as a string value
# example - '''hello'''

# in the string jhon's  to write the string we can use the double quotes
# example - "jhon's"


# indexing in the string  - the process of the accessing the character of the string using the index number
# the index number of the string always starts from the 0


# to find the length of string the len function is used

name = " harry "
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[0:5])
print(name[1:3])
print(len(name))
print(name[:3])
print(name[3:])
print(name[-3:])
print(name[-4:-1])
print(name[0:5:2])
print(name[0::2])
print(name[::2])
print(name[::])
#  functions in python
# |-------|------------|------------------------|
# | index | function   |     example            |
# |-------|------------|------------------------|
# | 1     | len        | len(name)              |
# | 2     | endswith   | name.endswith("y")     |
# | 3     | count      | name.count("a")        |
# | 4     | capitalize | name.capitalize()      |
# | 5     | find       | name.find("h")         |
# | 6     | replace    | name.replace("h", "p") |
# | 7     | upper      | name.upper()           |
# | 8     | lower      | name.lower()           |
# | 9     | title      | name.title()           |
# | 10    | swapcase   | name.swapcase()        |
# | 11    | center     | name.center(100)       |
# | 12    | lstrip     | name.lstrip()          |
# | 13    | rstrip     | name.rstrip()          |
# | 14    | strip      | name.strip()           |
# | 15    | split      | name.split()           |
# | 16    | join       | name.join()            |
# |-------|------------|------------------------|


story = "once upon a time there was a king in the jungle"
print(len(story))

# 1. len - the function that is used to find the length of the string
print(story.endswith("jungle"))

# 2. endswith - the function that is used to check the string ends with the given string
print(story.count("a"))

# 3. capitalize - the function that is used to capitalize the first letter of the string
print(story.capitalize())

# 4. find - the function that is used to find the index of the given string
print(story.find("upon"))

# 5. replace - the function that is used to replace the string with the given string
print(story.replace("king", "queen"))
print(story.replace("a", "the"))
print(story.replace("a", "the", 2))

# 6. upper - the function that is used to convert the string into the upper case
print(story.upper())

# 7. lower - the function that is used to convert the string into the lower case
print(story.lower())

# 8. title - the function that is used to convert the string into the title case
print(story.title())

# 9. swapcase - the function that is used to swap the case of the string
print(story.swapcase())

# 10. center - the function that is used to center the string
print(story.center(100))

# 10. lstrip - the function that is used to remove the left side space of the string
print(story.lstrip())

# 11. retrip - the function that is used to remove the right side space of the string
print(story.rstrip())

# 12. strip - the function that is used to remove the space of the string
print(story.strip())

# 13. split - the function that is used to split the string
print(story.split())
print(story.split("a"))
print(story.split("a", 2))
print(story.join("a"))

# 14. join - the function that is used to join the string
print(" ".join(story))
print(" ".join(story.split()))
print(" ".join(story.split("a")))
print(" ".join(story.split("a", 2)))

# 15. isalnum - the function that is used to check the string is alphanumeric or not
print(story.isalnum())
