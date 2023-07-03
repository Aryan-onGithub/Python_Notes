l1 = [3, 5, 11, 2, "aryan"]

#strings are made to call multiple values using single variable
#string can store values having different data types
#list have multiple methods
#list are mutable, can be changed after being created
#don't create new sting after using list methods but modify the existing string
print(l1)
print(type(l1))

'''List methods,  few examples '''
print(l1.count(2))
l1.remove("aryan")
l1.append(21) #add one value
l1.extend([66, 54, 63]) #add multiple values
l1.sort()
print(l1)
l1.pop()
print(l1)
print("3 is at index",l1.index(3))
l1[0]= "aryan"
print(l1)

#and meny more methods
