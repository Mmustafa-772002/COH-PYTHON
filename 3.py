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
print(name[1:3 ])
print(len(name))
print(name[:3])
print(name[3:])
print(name[-3:])
print(name[-4:-1])
print(name[0:5:2])
print(name[0::2])
print(name[::2])
print(name[::])


story = "once upon a time there was a king in the jungle"
print(len(story))
# len - the function that is used to find the length of the string
print(story.endswith("jungle"))
# endswith - the function that is used to check the string ends with the given string
print(story.count("a"))
# capitalize - the function that is used to capitalize the first letter of the string
print(story.capitalize())
# find - the function that is used to find the index of the given string
print(story.find("upon"))
# replace - the function that is used to replace the string with the given string
print(story.replace("king", "queen"))
print(story.replace("a", "the"))
print(story.replace("a", "the", 2))
# upper - the function that is used to convert the string into the upper case
print(story.upper())
# lower - the function that is used to convert the string into the lower case
print(story.lower())
# title - the function that is used to convert the string into the title case
print(story.title())
# swapcase - the function that is used to swap the case of the string
print(story.swapcase())
# center - the function that is used to center the string
print(story.center(100))
# lstrip - the function that is used to remove the left side space of the string
print(story.lstrip())
# retrip - the function that is used to remove the right side space of the string
print(story.rstrip())
# strip - the function that is used to remove the space of the string
print(story.strip())
# split - the function that is used to split the string
print(story.split())
print(story.split("a"))
print(story.split("a", 2))
print(story.join("a"))

