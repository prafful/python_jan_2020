friends = []
print(friends)
print(type(friends))

friends = ["Oki", "moki", 1, 2]
print(friends)

score = [20, 40, 80, 44]
print(score)

#create list using list() function
check = list([54, 87, 12, 1, 56])
print(check)
print(len(check))

# combining two lists
newList = list([friends, score, check])
print(newList)

# multi-dimensional list

mdl = [6]*3
print(mdl)

#mdl2 = [mdl]*3  
mdl2 = [[6]*3]*3
print(mdl2) 

'''
[
    [6, 6, 6],  #0,0 to 0,2 -> mdl2[0]
    [6, 6, 6],  #1,0 to 1,2 -> mdl2[1]
    [6, 6, 6]   #2,0 to 2,2 -> mdl2[2]
]
'''
#mdl2[0], mdl2[1] and mdl2[2] are clones at same memory location
print(id(mdl))
print(id(mdl2))
print(id(mdl2[0]))
print(id(mdl2[1]))
print(id(mdl2[2]))
mdl2[0][1] = 4
print(mdl2)

#check again

mdl3 = [[1,2,3],[4,5,6],[7,8,9]]
mdl3[2][2] = 10
print(mdl3)

#list addition
col1 = ['a','e','i','o','u']
col2 = ["amar", "akbar", 3.5]

col3 = col1 + col2
print(col3)
#using extend
col3 = col1.extend(col2)
#col3 will point to none
print(col3)
print(col1)
#using append
col1.append(col2)
print(col1)

print(col2)
print(col2[-3])

#skipping items
col1 = ['a','e','i','o','u', 'q','w','e','r','t','y']
#print(col1[2:9:1]) //check this syntax

#list traversing
for n in col1:
    print(n)

col2 = ["amar", "akbar", 3.5]
#print(col2.next())    # error - list object has not attribute next
#it = iter(col2) # create iterator from list object
#check = it.next()

#insert in list
col2.insert(2, "antony")
print(col2)

#insert using slice operator
col1 = ['a','e','i','o','u', 'q','w','e','r','t','y']
col1[2:8] = ['1','2']
# [a','e','1','2','i','o','u', 'q','w','e','r','t','y']]
print(col1)

#del items from list
col1 = ['a','e','i','o','u', 'q','w','e','r','t','y']
del col1[0]  #use index poistion to delete item
print(col1)

#use value to delete item
print(col1.remove('o'))
print(col1)

#pop the item at given position
print(col1.pop(5))
print(col1)

#searching list with in operator
value = 'r'
if value in col1:
    print("col1 contains ", value)
else:
    print("col1 not contains ", value)    


#use index to get first index when given item is found
print(col1.index('r'))

col1.sort()
print(col1)
col1.reverse()
print(col1)

check = list([54, 87, 12, 1, 56])
check.sort()
print(check)
check.reverse()
print(check)


# delete list
#del col1
#print(col1)

