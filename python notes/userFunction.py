'''def name()'''#syntax

def myFun():          #defining function
    print("hello")

myFun()               #function calling

def myFun2(name, time):   #function arguements
    print("Good " + time + " "+ name.capitalize())

myFun2("aryna", "morning")
myFun2("palak", "evening")

''' making a leave application template'''

def letterGenerator(name, date):
    st = f"Hi mam,\nMy nam is {name.capitalize()} and i will not come to school on {date}"
    print(st)
#we used a f-string in this example
#f-String is a string which can store variables and escape sequences(\n, \t, etc,) which can then be replaced by their values

letterGenerator("aryan", "17 june2023")

'''function to return value'''

def avg(n1, n2):
    return (n1+n2)/2

print(avg(5, 7))