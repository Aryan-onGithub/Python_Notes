a = {3, 5, 5, 6, 32, 1, 4}
#sets are same as set theory in mathamatics, read set theory to understand all methods of sets
b = {3, 5, 5, 44, 23, 64, 6}
c = set() #to make an empty set
print(a)
print(a.pop()) #takes our a random element
print(a)

'''set methods, few examples'''
a.add("aryan")
print(a.union(b))
print(a.intersection(b))
print(a.issuperset(b))
print(a.issubset(b))