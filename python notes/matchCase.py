a = int(input("Enter a number between 1 to 4: "))

match a :
    case 1:
        print("case in 1")
    case 2:
        print("case in 2")
    case 3:
        print("case in 3")
    case 4:
        print("case in 4")
    case _:   #default, not necessary to write
        print("you are a moron")

#Match case statement is new in python after 3.10 update and
#it is used to make things more convenient and fast

'''Quick quiz: write a python program to print table of a number which lies between 1 to 10'''

num = int(input("Enter a number: "))

match num:
    case 1:
        b = num
    case 2:
        b = num
    case 3:
        b = num
    case 4:
        b = num
    case 5:
        b = num
    case 6:
        b = num
    case 7:
        b = num
    case 8:
        b = num
    case 9:
        b = num
    case 10:
        b = num

print("1 x 1 = ",b*1)
print("1 x 2 = ",b*2)
print("1 x 3 = ",b*3)
print("1 x 4 = ",b*4)
print("1 x 5 = ",b*5)
print("1 x 6 = ",b*6)
print("1 x 7 = ",b*7)
print("1 x 8 = ",b*8)
print("1 x 9 = ",b*9)
print("1 x 10 = ",b*10)