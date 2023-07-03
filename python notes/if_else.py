#syntax
if(2>3):
    print("yes")    #space represent the indentation
else:
    print("no")

age = int(input("write your age:"))

if(age>=18):
    print("you can vote")
elif(age == 15):
    print("you are a teenager")
elif(age == 1):
    print("you are a kid")
else:
    print("you can not vote")

#if-else ladder works till it finds else
#we can add elif to add multiple cases

a = True
if(a==True):
    print("we can write if without elif or else")

#we cannot write elif and else without if

b=True

if(b==False):
    print(none)
elif(b==True):
    print("we can write elfe without else but require if")






