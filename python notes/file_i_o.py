#we use file i/o to read, write, append somenting in a file

s = "My name is: Aryan Chandra"
with open("test.txt", "w") as f:
    f.write(s)
    #this code created a file name test.txt and write string s inside it

#"with" is context manager, we use it to not write closing statement
#"open" is used to open file
#open("file name", "mode"), their are mainly three modes w(write), r(read), a(append)
#as "f" is an object created to call this function
#open will create a file if the file does not exists

# r : read a file
# w : replacing anything written in file with what you write
# a : add things you write with the already written thing in file

'''we can also do the same process without using with'''
fp = open("test.txt", "w")   #fp is a variable used call open and use methods
fp.write(s)
fp.close()  #we need to use close ethod as we didnt use with context manager

'''using read mode'''

with open("test.txt", "r") as f:
    st = f.read()
    print(st)

# or

fc = open("test.txt", "r")
s = fc.read()
print(s)
fc.close()

'''using append mode'''
#everything same as write, just replace r with a mode
str2 = "and i love py"
with open("test.txt", "a") as e:
         e.write(str2)

#append mode don/t erase previously written things in the file


#thier are many other fuction in i/o but these methods are mostly used
