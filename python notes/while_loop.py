a = 1
while(a<5):    #syntax
    print(a)
    a+=1

'''while(condition)'''

#to create a infinite while loop while loop give condition as True

# while(True):
#     print("this is a infinite while loop")

#we can use break statement to end infinite while loop

while(True):
    num = int(input("enter a number: "))
    if(num == 0):
        print("loop ended")
        break    #use to exit a program in a given scope
    else:
        print("number is: ", num )