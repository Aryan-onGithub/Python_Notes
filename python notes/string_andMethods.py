name = 'aryan'  #we can use '' or "" to write string
name2 = "47"

print(name+name2)

#strings are immutable, can't be changed once made
#when ever we use sting methods we create a new string not modify the existing string
'''String slicing'''
print(name[0:3]) #Start form index 0 and got till 2 (3-1)
# print(name[a:b]) #Start form index a and got till b (b-1)

''' String methods '''
#we can search python doc (docs.python.org) to find latest string method for python version
#their are multiple string methods in python
#some pyhton methods examples

print(name.upper()) #makes all charactor capital
print(name.capitalize()) #makes first charactor capital
print(name.count("a")) #gives a number of time a charactor has arrived in string
print(name.isalnum())
print(name2.isalnum())
print(name.isnumeric())
print(name2.isnumeric())
print("name is",not(name.isnumeric()))
print(name.swapcase())  #change string charactor form uppercase to lowercase and vice versa

#we can hovver over sting methods to know what it does, you also get a link to python docs for detailed info

st = f"Hi mam,\nMy nam is {name.capitalize()} and i will not come to school on {date}"
    print(st)
#we used a f-string in this example
#f-String is a string which can store variables and escape sequences(\n, \t, etc,) which can then be replaced by their values