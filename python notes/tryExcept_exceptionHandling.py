#try except is used if their are chances that your code can give an error

a = int(input("Enter your number: "))
print(a+3)
#the above code can only take input which are integer
#if we put any other data type like string then it will give an error

#we use exception handeling to escape these errors, as they freeze our program and we dont want that

'''we use "try" and "except to hande exceptions'''

try:      #write code which can give error
    b = int(input("Enter your number: "))
    print(b + 3)
except:   #run the below code instead if the code gave error
    print("Please provide an integer value")

#this code will not give an error if we put any other datatype other then integer

#we can also print the error that occer by writing
try:
    c = int(input("Enter your number: "))
    print(b + 3)
except Exception as e:   #e stores type of error
    print("error occered", e)