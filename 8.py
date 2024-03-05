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

fruit = ["apple", "banana", "cherry"]
i = 0 
while i < len(fruit):
    print(fruit[i])
    i = i+1

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

# q -  print the numbers from 1 to 10 using for loop
for i in range(1,11):
    print(str(i))
print("done")

# q -  print the numbers from 10 to 1 using for loop
for i in range(10,0, -1):
    print(str(i))
print("done")

for i in range(1, 11,2):
    print(str(i))
print("done")

for i in range(2,20 ,2):
    print(str(i))
print("done")

# for loop in else statement - the else statement is used to execute the code block once the condition is false.

for i in range(1, 11):
    print(str(i))
else:
    print("done the stmt is executed")
#   it is the optional else in the for loop  

# break - the break statement is used to terminate the loop once the condition is true.

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("done")

# continue - the continue statement is used to skip the current iteration and continue with the next iteration.

for i in range(10):
    if i == 5:
        continue
    print(i)
else:
    print("done")

# pass - the pass statement is used to execute the empty code block.

for i in range(10):
    pass
else:
    print("done")
    
for i in range(10):
    if i == 5:
        pass
    while i == 5:
        print(i)
        break
else:
    print("done")
    
# nested loops - the nested loops are the loops that are used inside the other loop.
# q - print the table from 1 to 10 using nested loops
for i in range(1, 11):
    for j in range(1, 11):
        print(str(i) + " * " + str(j) + " = " + str(i*j))
    print("done")
    
# q - print the table from 1 to 10 using nested loops
num = int(input("enter the number: "))
for i in range(1, 11):
    print(str(num) + " * " + str(i) + " = " + str(num*i))

l1 =["harry", "sohan", "sachin", "mohan"]
for name in l1:
    if name.startswith("s"):
        print("hello " + name)
    else:
        print("bye " + name)
        
# q - check the number is prime or not
num = int(input("enter the number: "))
prime = True 
for i in range (2,num):
    if num%i==0:
        prime = False
        break
if prime:
    print("the number is prime")
else:
    print("the number is not prime")

# q - to check the number is factorial or not
num = int(input("enter the number: "))
fact = 1
for i in range(1,num+1):
    fact =fact*1
print("the factorial of the number is " + str(fact))    

# q - print a star pattern 
n = 5
for i in range(n):
    print("*" * (i+1))
    
i = int(input("enter the number of star to be printed: "))

for i in range(i):
    print("*" *(i+1))
    

i=int(input("enter the number of star to be printed: "))
for i in range(i):
    print("*" * (i+1))
    
# pyramid star pattern
i = int(input("enter the number of star to be printed: "))
for j in range(i):
    print(" " * (i-j-1) + "*" * (2*j+1))
    
    # sqare star pattern
i = int(input("enter the number of star to be printed: "))
for j in range(i):
    print("*" * i)


# to make a square star pattern with the hollow center

i = int(input("enter the number of star to be printed: "))
for j in range(i):
    if j ==0 or j ==i-1:
        print("* " *i)
    else:
        print("*"+" " *(i-2)+"*")
        
# multiplication table in reverse order
a = int(input("enter the start number: "))
b = int(input("enter the end number: "))
c = int(input("enter the multiplication number: "))
for i in range(b-a+1):
    print(str(c)+"*"+str(b-i)+"="+str(c*(b-i))   )