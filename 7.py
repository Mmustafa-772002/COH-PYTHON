# conditional stmt - if, elif, else
# these are the conditional statements in python  that are used to make decisions based on the given condition.
# if else are the multiple decision taken in the program due to certain condition on the code block.
# syntax of if else:
# if condition:
#     code block
# elif condition:
#     code block
# else:
#     code block

# if else with the conditions in the program:
# if else - multiple decision taken in the program due to certain condition on the code block. 
# syntax  - 
# if condition:
#     code block
# else:
#     code block

# nested if else - if else statements are used inside the if else statements.
# syntax -
# if condition:
#     code block
#     if condition:
#         code block
#     else:
#         code block
# else:
#     code block

# multiple if statements - if else statements are used to check the multiple conditions in the program.
# syntax -
# if condition:
#     code block
# if condition:
#     code block
# else:
#     code block

# if else with logical operators - logical operators are used to check the multiple conditions in the program.
# syntax -
# if condition and condition:
#     code block
# else:
#     code block

# if else with in operator - in operator is used to check the multiple conditions in the program.
# syntax -
# if condition in range():
#     code block
# else:
#     code block

# if else with not in operator - not in operator is used to check the multiple conditions in the program.
# syntax -
# if condition not in range():
#     code block
# else:
#     code block

# if else with is operator - is operator is used to check the multiple conditions in the program.
# syntax -
# if condition is value:
#     code block
# else:
#     code block

# if else with is not operator - is not operator is used to check the multiple conditions in the program. 
# syntax -
# if condition is not value:
#     code block    
# else:
#     code block

# if else with pass statement - pass statement is used to check the multiple conditions in the program. 
# syntax -
# if condition:
#     pass
# else:
#     code block

# if else with assert statement - assert statement is used to check the multiple conditions in the program. 
# syntax -
# if condition:
#     assert condition, "message"
# else:
#     code block




s = 45
if s > 10:
    print("s is greater than 10")
elif s < 10:
    print("s is less than 10")
else:
    print("s is equal to 10")  

# multiple if statements: in this case, the multiple if statements are used to check the multiple conditions in the program. 

s = 45
if s > 10:
    print("s is greater than 10")
if s < 10:
    print("s is less than 10")
else:
    print("s is equal to 10")

# nested if else:   
# in this case, the if else statements are used inside the if else statements.

s = 45
if s > 10:
    print("s is greater than 10")
    if s < 10:
        print("s is less than 10")
    else:
        print("s is equal to 10")
else:
    print("s is less than 10")
    
# if else with logical operators: in this case, the logical operators are used to check the multiple conditions in the program.

s = 45
if s > 10 and s < 50:
    print("s is greater than 10 and less than 50")
else:
    print("s is less than 10 or greater than 50")
    
    
# if else with in operator: in this case, the in operator is used to check the multiple conditions in the program.

s = 45
if s in range(10, 50):
    print("s is in the range of 10 and 50")
else:
    print("s is not in the range of 10 and 50")
    
# if else with not in operator: in this case, the not in operator is used to check the multiple conditions in the program.

s = 45
if s not in range(10, 50):
    print("s is not in the range of 10 and 50")
else:
    print("s is in the range of 10 and 50")
    
# if else with is operator: in this case, the is operator is used to check the multiple conditions in the program.

s = 45
if s is 45:
    print("s is 45")
else:
    print("s is not 45")
    
# if else with is not operator: in this case, the is not operator is used to check the multiple conditions in the program.

s = 45
if s is not 45:
    print("s is not 45")
else:
    print("s is 45")
    
# if else with pass statement: in this case, the pass statement is used to check the multiple conditions in the program.

s = 45
if s > 10:
    pass
else:
    print("s is less than 10")
    
# if else with assert statement: in this case, the assert statement is used to check the multiple conditions in the program.

s = 45
assert s > 10, "s is less than 10"
print("s is greater than 10")

# if else with assert statement: in this case, the assert statement is used to check the multiple conditions in the program.

s = 45
assert s < 10, "s is less than 10"
print("s is greater than 10")


