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


a = [45, 20, 5]
print(45 in a)

# in the if else code stmt the else is the optional and the elif is also the optional. and the if else stmt is used to make the decision based on the given condition

# q - write the program to find the greatest four number entered by the user

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
d = int(input("enter the fourth number: "))

if a > b and a > c and a > d:
    print("a is the greatest number")
elif b > c and b > d and b > a:
    print("b is the greatest number")
elif c > d and c > a and c > b:
    print("c is the greatest number")
elif d > a and d > b and d > c:
    print("d is the greatest number")
else:
    print("all the numbers are equal")

# q - write the program to find the greatest number entered by the user in multiple if else stmt
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
num4 = int(input("enter the fourth number: "))
if num1 > num4:
    f1 = num1
else:
    f1 = num4
if num2 > num3:
    f2 = num2
else:
    f2 = num3
if f1 > f2:
    print(str(f1) + " is the greatest number")
else:
    print(str(f2) + " is the greatest number")


# q - to find out the stmt is pass or fail based on if it requires 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("enter the marks of the first subject: "))
sub2 = int(input("enter the marks of the second subject: "))
sub3 = int(input("enter the marks of the third subject: "))
if sub1 <= 33 or sub2 <= 33 or sub3 <= 33:
    print(" you are fail due to less than 33% in one of the subject")
    if (sub1 + sub2 + sub3) / 3 < 40:
        print("fail")
    else:
        print("pass")

#  q - a spam comment is defined as a text containing the following keywords: make a lot of money, buy now, subscribe this, click this, and many more. Write a program to detect these spam comments.

comment = input("enter the comment: ")
if "make a lot of money" in comment:
    spam = True
elif "buy now" in comment:
    spam = True
elif "subscribe this" in comment:
    spam = True
elif "click this" in comment:
    spam = True
else:
    spam = False
if spam:
    print("spam comment")
else:
    print("not a spam comment")

#  q  - to cheack the gibven number is positive or negative
num = int(input("enter the number: "))
if num > 0:
    print("positive number")
else:
    print("negative number")

# q - to check the given number is even or odd
num = int(input("enter the number: "))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# q - to check the given number is divisible by 5 or not
num = int(input("enter the number: "))

if num % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")

# q - to check the given number is divisible by 5 and 11 or not
num = int(input("enter the number: "))
if num % 5 == 0 and num % 11 == 0:
    print("divisible by 5 and 11")
else:
    print("not divisible by 5 and 11")

# q - to check the given number is divisible by 5 or 11 but not both
num = int(input("enter the number: "))
if num % 5 == 0 or num % 11 == 0:
    print("divisible by 5 or 11")
else:
    print("not divisible by 5 or 11")

    # q - to check the name is present in the list or not
name = input("enter the name: ")
names = ["harry", "rohit", "mohit", "sohit", "mohit"]
if name in names:
    print("name is present in the list")
else:
    print("name is not present in the list")
