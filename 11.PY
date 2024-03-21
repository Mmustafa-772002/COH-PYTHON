# FILE I/O :  this is the process of reading and writing to files on the computer. the file is a container for storing data. 
# in order to work with files in python, we need to open the file. a file can be opened in read mode, write mode, append mode, or a combination of these modes. 

#  there is two types of files in python: text files and binary files.
#  text files: a file that contains only printable characters and white spaces.

# example : text files include files that end with .txt, .py, .html, .css, .js, .csv, .json, .xml, etc.

#  binary files: a file that contains binary data.

# example :  binary files include files that end with .jpg, .png, .mp3, .mp4, .pdf, .doc, .xls, .exe, etc.

#  when we open a file, we need to specify the mode in which we want to open the file.

# opening files in python: python has a built-in function called open() that allows us to open files. the open() function returns a file object that represents the file we want to open. 

# syntax: file_object = open(file_name, mode)
#  by default, the open() function opens the file in read mode.

file = open('demofile.txt','r')
# data = file.read()
data = file.readline()
data = file.readlines()

print(data)
file.close()

# file = open('demofile.txt','r')
# new = file.read(5)
# print(new) 
# file.close()

# modes of them opening files : 
# 'r' : read mode. this is the default mode. it opens the file for reading.
# example : file = open('demofile.txt','r')

# 'w' : write mode. it opens the file for writing. if the file does not exist, it creates a new file. if the file exists, it truncates the file.
# example : file = open('demofile.txt','w')

# 'x' : create mode. it creates the specified file. if the file already exists, the operation fails.
# example : file = open('demofile.txt','x')

# 'a' : append mode. it opens the file for appending. if the file does not exist, it creates a new file.
# example : file = open('demofile.txt','a')

# 't' : text mode. this is the default mode. it opens the file in text mode.
# example : file = open('demofile.txt','r')

# 'b' : binary mode. it opens the file in binary mode.
# example : file = open('demofile.txt','rb')

# '+' : read and write mode. it opens the file for reading and writing.
# example : file = open('demofile.txt','r+')

# file = open('demofile.txt','w')
# example :# file.write('hello world')
# file.close()

# file = open('demofile.txt','a')
# file.write('hello world')
# file.close()

# file = open('demofile.txt','r+')
# print(file.read())
# file.write('hello world')
# file.close()

# file = open('demofile.txt','w+')
# file.write('hello world')
# print(file.read())
# file.close()

# file = open('demofile.txt','a+')
# file.write('hello world')
# print(file.read())
# file.close()

# file = open('demofile.txt','x')
# file.write('hello world')
# file.close()

# file = open('demofile.txt','rt')
# file = open('demofile.txt','rb')
# file = open('demofile.txt','r+t')
# file = open('demofile.txt','r+b')
# file = open('demofile.txt','w+t')
# file = open('demofile.txt','w+b')
# file = open('demofile.txt','a+t')

file = open('demofile.txt','w')
file.write('please write the content in the file')  # this will overwrite the content of the file.
file.close()

file = open('demofile.txt','a')
file.write("\ni am appending the text files ")  # this will overwrite the content of the file.
file.close()

with open('demofile.txt','a') as file:
    file.write("\nthis is the new line")
    
f =open('demofile.txt','r')
t= f.read()
if 'this ' in t:
    print('yes')
else:
    print('no')
f.close()

def game():
    return 88
# file = open('highscore.txt','x')
# file.write(str(game()))
# file.close()

score = game ()
with open('highscore.txt') as f :
    highscorestr = f.read()
    
if highscorestr =="": 
    with open('highscore.txt','w') as f:
        f.write(str(score))
        print('you have broken the highscore')

elif int(highscorestr) < score: 
    with open('highscore.txt','w') as f:
        f.write(str(score))
        print('you have broken the highscore')

for i in range(2,21):
    with open("table/table of "+str(i),'w') as f:
        for j in range(11):
            f.write(f"{i}X{j}={i*j}\n") 
    break  

i = int(input("Enter the number: "))
for i in range(i,i+1):
    with open("table/table of "+str(i),'w') as f:
        for j in range(11):
            f.write(f"{i}X{j}={i*j}\n") 
    break  

i = int(input(" enter a number : "))
for i  in range(i, i+1):
    with open("table/table of " + str(i),"w") as f:
        for i in range(11):
            f.write(f"{i}x{j}={i*j}\n")
    break

#  to check the wrong word in the file and replace it with the correct word. such as donkey with monkey.
with open('demofile.txt','r') as f:
    content = f.read()
# this is replacing the word in the file. the replace function is used to replace the word in the file.
content = content.replace('hello','monkey')

with open('demofile.txt','w') as f:
    f.write(content)

        

