#class, objects, function, methods

#classes are like template used to create objects
class Employee:
    salary = 500
    name = "aryan"

aryan = Employee()   #aryan is an object
print(aryan.salary)  #salary is an variable called in objct aryan
print(aryan.name)

#in the above example we called the name and salary directly from the class, but they will be same for all the objects we create, which we don't want
"_____________________________________"
class Emplayee2:
    def __init__(self, name, salary):    #construction function
#name and salary are the arguements we passed inside the function and to call them we write self.
        self.name = name
        self.salary = salary
#self is always the first arguement we take to write a function inside a class

    def getSalary(self):
        print(self.salary) #this wil print the salary of an object
#this is how we create a function inside a class and to call define variable inside it we have to write self.

rohan = Emplayee2("rohan", "5000")  #we didnt write the function used as it was constructor and it is called automatically whenever a object is created for that class
print(rohan.salary)  #this will print salary of rohan we provided in the arguement and this way we can have different calues for different objects
print(rohan.name)
rohan.getSalary() #this checked what is rohan salary ade go into getSalary function and printed salary as commanded

aryan = Emplayee2("Aryan", "500000")
aryan.getSalary()


#thier are more in classes and objects, but this knowledge is enough for a begineer
#oops are not used that much in pythin in the feilds of ML, Data science