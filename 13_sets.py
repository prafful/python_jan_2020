friends = {'omi', 'lika', 'reks', 'mika','ola'}
print(type(friends))
print(friends)

# TypeError: unhashable type: 'list'
#mixed = {'ona', 1, 55.3, [1,2,3]}
mixed = {'ona', 1, 55.3, "[1,2,3]"}
print(mixed)

duplicates = {25, 35, 25, 25, 35, 1}
print(duplicates)

checkThis = set([25, 35, 44.4, "diong"])
print(checkThis)
checkThis.remove("diong")
print(checkThis)
#checkThis.remove("diong")
#print(checkThis)
checkThis.discard("diong")
print(checkThis)

""" 
print(type(checkThis))
print(checkThis)
print(checkThis.pop())
checkThis.add("me")
print(checkThis)
print(checkThis.pop())

print(id(checkThis))
checkThis.remove("diong")
print(checkThis) """

checkThis.clear()
print(checkThis)

set1 = {'a','e','i','o','u', 'q'}
set2 = {'w','e','r','t','y'}

set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)
# return those elements from set2 which are
# not in set1
set3 = set2 - set1
print(set3)
# return those elements from set1 which are
# not in set2
set3 = set1 - set2
print(set3)