a = {1,2,3,4}
b = {}   #dictionary syntex

print(type(a))
print(type(b))

#dictionary are key value pairs

dict1 = {"aryan": 20,"palak":17, "lucy": 12}
print(dict1) #print dictonary
print(dict1["aryan"]) #print key element

#we can use dictionary in meny ways, for ex- storing marks of students

# Dictionary = {"keys" : values}

#dictionary are mutable, values can be modified

dict1["aadi"] = 14 #adding key and value
print(dict1["aadi"])

''' Dictionary methods, few examples'''
print(dict1.get("aryan"))
print(dict1.get("aryman")) #if aryman is not present in the dictionary then it will give "none" as its value

#print(dict1["aryman"]) #will get an error if run this and the key is not present in the dictionary

print(dict1.keys()) #print all keys present in the dictionary

print(dict1.values())

print(dict1.items()) #give key and value in pairs


