# loops in python -
# the loops are the set of repetitive statements in the program that are used to execute the same code block multiple times.
# while loop - while loop is used to execute the code block until the condition is true.
# syntax -
# while condition:
#     code block
#
# print upto 10 numbers using while loop
i = 1
j = 10
while i <= j:
    print(str(i))
    i = i+1
print("done ")

# multiple conditions in the program
a = int(input("enter the starting value : "))
b = int(input("enter the end value: "))
while a<=b:
    print(str(a))
    a=a+1
print("done")

# to print the numbers in reverse order
i = 10
j = 1
while i >= j:
    print(str(i))
    i = i-1
print("done")

# to print the table and the basic calculation 
a = int(input("enter the start number: "))
b = int (input("enter the end number: ")) 
c= int(input("enter the multiplication number: ")) 
while a<=b:
    print(str(c) + " * " + str(a) + " = " + str(a*c))
    a=a+1
print("done") 
    
    
    # for loop - for loop is used to execute the code block until the condition is true.
# syntax -
# for variable in range():
#     code block
#
