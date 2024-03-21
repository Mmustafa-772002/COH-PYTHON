# variables and data types
# variable - a variable is give to a memory location to store the data
# it is the container that is  used to store the data
a = " harry"
# it is variable of the string type
b = 35
# it is the type of int data
c = 45.5

# keyword - it is a special word that is reserved by the python
# it is used to perform the specific task
# it is case sensitive
# it is the predefined word
# it is the reserved word
# the list of the keywords in the python
# there are 35 keywords in the python
# |-------|--------------|------------------|
# | index |  keyword     |      example     |
# |-------|--------------|------------------|
# | 1     |  false       |  False           |
# | 2     |  none        |  None            |
# | 3     |  true        |  True            |
# | 4     |  and         |  a and b         |
# | 5     |  as          |  import a as b   |
# | 6     |  assert      |  assert a > b    |
# | 7     |  break       |  break           |
# | 8     |  class       |  class a         |
# | 9     |  continue    |  continue        |
# | 10    |  def         |  def a           |
# | 11    |  del         |  del a           |
# | 12    |  elif        |  elif a > b      |
# | 13    |  else        |  else            |
# | 14    |  except      |  except          |
# | 15    |  finally     |  finally         |
# | 16    |  for         |  for a in b      |
# | 17    |  from        |  from a import b |
# | 18    |  global      |  global a        |
# | 19    |  if          |  if a > b        |
# | 20    |  import      |  import a        |
# | 21    |  in          |  in a            |
# | 22    |  is          |  a is b          |
# | 23    |  lambda      |  lambda a        |
# | 24    |  nonlocal    |  nonlocal a      |
# | 25    |  not         |  not a           |
# | 26    |  or          |  a or b          |
# | 27    |  pass        |  pass            |
# | 28    |  raise       |  raise           |
# | 29    |  return      |  return a        |
# | 30    |  try         |  try             |
# | 31    |  while       |  while a > b     |
# | 32    |  with        |  with a as b     |
# | 33    |  yield       |  yield a         |
# | 34    |  print       |  print a         |
# | 35    |  input       |  input a         |
# |-------|--------------|------------------|

# 1. false - it is the keyword that is used to represent the false value
# 2. none - it is the keyword that is used to represent the null value
# 3. true - it is the keyword that is used to represent the true value
# 4. and - it is the keyword that is used to perform the logical and operation
# 5. as - it is the keyword that is used to give the alias name to the module
# 6. assert - it is the keyword that is used to check the condition
# 7. break - it is the keyword that is used to break the loop
# 8. class - it is the keyword that is used to define the class
# 9. continue - it is the keyword that is used to continue the loop
# 10. def - it is the keyword that is used to define the function
# 11. del - it is the keyword that is used to delete the object
# 12. elif - it is the keyword that is used to check the multiple condition
# 13. else - it is the keyword that is used to check the condition
# 14. except - it is the keyword that is used to handle the exception
# 15. finally - it is the keyword that is used to execute the block of code
# 16. for - it is the keyword that is used to iterate the loop
# 17. from - it is the keyword that is used to import the module
# 18. global - it is the keyword that is used to declare the global variable
# 19. if - it is the keyword that is used to check the condition
# 20. import - it is the keyword that is used to import the module
# 21. in - it is the keyword that is used to check the value in the sequence
# 22. is - it is the keyword that is used to check the identity
# 23. lambda - it is the keyword that is used to define the anonymous function
# 24. nonlocal - it is the keyword that is used to declare the nonlocal variable
# 25. not - it is the keyword that is used to perform the logical not operation
# 26. or - it is the keyword that is used to perform the logical or operation
# 27. pass - it is the keyword that is used to define the empty block
# 28. raise - it is the keyword that is used to raise the exception
# 29. return - it is the keyword that is used to return the value
# 30. try - it is the keyword that is used to test the block of code
# 31. while - it is the keyword that is used to iterate the loop
# 32. with - it is the keyword that is used to wrap the execution
# 33. yield - it is the keyword that is used to return the value from the generator
# 34. print - it is the keyword that is used to print the value
# 35. input - it is the keyword that is used to take the input from the user

# identifiers - the name of the variable, function, class, module, etc is called the identifier
# |-------|------------------|------------------|
# | index |  identifier      |      example     |
# |-------|------------------|------------------|
# | 1     |  variable        |  a = 10          |
# | 2     |  function        |  def a():        |
# | 3     |  class           |  class a:        |
# | 4     |  module          |  import a        |
# | 5     |  object          |  a = A()         |
# | 6     |  package         |  import a.b      |
# | 7     |  method          |  a.b()           |
# | 8     |  constant        |  PI = 3.14       |
# | 9     |  attribute       |  a.b             |
# | 10    |  argument        |  a(b)            |
# | 11    |  keyword         |  if,else,for     |
# | 12    |  expression      |  a + b           |
# | 13    |  statement       |  a = 10          |
# | 14    |  block           |  {a = 10}        |
# | 15    |  indentation     |  4 space         |
# | 16    |  suite           |  a = 10          |
# | 17    |  loop            |  for a in b:     |
# | 18    |  conditional     |  if a > b:       |
# | 19    |  control         |  break,continue  |
# | 20    |  exception       |  try,except      |
# | 21    |  comment         |  # comment       |
# | 22    |  docstring       |  '''docstring''' |
# | 23    |  literal         |  10,"hello",3.14 |
# | 24    |  operator        |  +,-,*,/,%       |
# | 25    |  delimiter       |  :,(,),{,}       |
# |-------|------------------|------------------|

# class - class is a blueprint for the object
# data type - the type of the data that is stored in the variable
# there are 14 types of data types in the python
# | ------- | ------------------ | ------------------ |
# | index   |  data type         |      example       |
# | ------- | ------------------ | ------------------ |
# | 1       |  int               |  a = 10            |
# | 2       |  float             |  a = 10.5          |
# | 3       |  str               |  a = "hello"       |
# | 4       |  list              |  a = [1,2,3,4,5]   |
# | 5       |  tuple             |  a = (1,2,3,4,5)   |
# | 6       |  set               |  a = {1,2,3,4,5}   |
# | 7       |  dict              |  a = {1:"one"}     |
# | 8       |  bool              |  a = True          |
# | 9       |  complex           |  a = 3 + 5j        |
# | 10      |  bytes             |  a = b"hello"      |
# | 11      |  bytearray         |  a = bytearray(10) |
# | 12      |  range             |  a = range(10)     |
# | 13      |  frozenset         |  a = frozenset(a)  |
# | 14      |  None              |  a = None          |
# | ------- | ------------------ | ------------------ |

# 1. int - it is the data type that is used to store the integer value
# 2. float - it is the data type that is used to store the floating value
# 3. str - it is the data type that is used to store the string value
# 4. list - it is the data type that is used to store the multiple value
# 5. tuple - it is the data type that is used to store the multiple value
# 6. set - it is the data type that is used to store the multiple value
# 7. dict - it is the data type that is used to store the multiple value
# 8. bool - it is the data type that is used to store the boolean value
# 9. complex - it is the data type that is used to store the complex value
# 10. bytes - it is the data type that is used to store the bytes value
# 11. bytearray - it is the data type that is used to store the bytearray value
# 12. range - it is the data type that is used to store the range value
# 13. frozenset - it is the data type that is used to store the multiple value
# 14. None - it is the data type that is used to store the null value
# the type() is used to check the type of the variable

# the main types are 5
# 1. int
# 2. float
# 3. str
# 4. none
# 5. bool
# 6. complex 

a = " jhon"
b = 453
c = 45.5
d = None
e = True
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# the type function that can be used to check the type of the variable

# rules for the naming of the variable
# 1. a variable name can contain the alphabets, digits, and underscore
# example : a_1 = 10

# 2. a variable name can start with the alphabet and underscore
# example : _a = 10

# 3. a variable name can not start with the digit
# example : 1_a = 10

# 4. a variable name can not contain the special character
# example : a@ = 10

# 5. a variable name can not contain the keyword
# example : if = 10

# 6. a variable name can not contain the space
# example : a b = 10

# the varible name is case sensitive
# example : a = 10
# A = 20
# print(a)
# print(A)

# the variable name should be descriptive
# example : a = 10
# b = 20
# c = 30
# print(a)
# print(b)
# print(c)

print(3 + 5)

d = 3
e = 5
print(d + e)

# operator - the symbol that is used to perform the operation on the variable
# there are 7 types of operators in the python
# 1. arithmetic operator - the operator that is used to perform the arithmetic operation on the variable
# example : +,-,*,/,%,//,**

# 2. assignment operator - the operator that is used to assign the value to the variable
# example : =,+=,-=,*=,/=,%=,//=,**=

# 3. comparison operator - the operator that is used to compare the value of the variable
# example : ==,!=,>,<,>=,<=

# 4. logical operator - the operator that is used to perform the logical operation on the variable
# example : and,or,not

# 5. identity operator - the operator that is used to check the identity of the variable
# example : is,is not

# 6. membership operator - the operator that is used to check the membership of the variable
# example : in,not in

# 7. bitwise operator - the operator that is used to perform the bitwise operation on the variable
# example : &,|,^,~,<<,>>

# the arithmetic operator
# + - it is used to add the value
# - - it is used to subtract the value
# * - it is used to multiply the value
# / - it is used to divide the value
# % - it is used to give the remainder of the value
#  "// " - it is used to give the floor value of the value
# ** - it is used to give the power of the value
a = 3
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# the comparison operator
# == - it is used to check the value is equal or not
# != - it is used to check the value is not equal
# > - it is used to check the value is greater or not
# < - it is used to check the value is less or not
# >= - it is used to check the value is greater or equal
# <= - it is used to check the value is less or equal
a = 3
b = 5
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# the logical operator
# and - it is used to perform the logical and operation
# or - it is used to perform the logical or operation
# not - it is used to perform the logical not operation
a = 3
b = 5
c = 7
print(a > b and a > c)
print(a > b or a > c)
print(not a > b)


# type casting and typw cionversion - the process of the converting a data type into the another type

# example    a = 3
#           print(type(a))
#           b = float(a)
#           print(b)
#           print(type(b))

# input function - it is the function that is used to take the input from the user
# the input function always returns the string value
a = input("enter the number :")
print(a, type(a))

# the input function always returns the string value to convert the string value to the integer value we can use the int function

a = int(input("enter the number :"))
print(a, type(a))

b = input("enter your name :")
print(b, type(b))


# q -  add two number 
a = 20
b = 30
c = a + b
print("the sum of a and b is : " ,c)

# q - remainder of the two number
a = 20
b = 30
c = a % b
print("the remainder of a and b is : " ,c)

# q- take the input from the user and print the type of the input
a = input("enter the value :")
print(a, type(a))

# q - using comparison operator compare the two number
a = 20
b = 30
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)   
print(a <= b)

#  q - average of two number 
a = 20
b = 30
c = (a + b) / 2
print("the average of a and b is : " ,c)

# q - square of the number
a = 20
b = a ** 2
print("the square of a is : " ,b)