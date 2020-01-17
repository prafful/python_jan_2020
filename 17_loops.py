'''
for target_list in expression_list:
    pass

'''
vovels = 'aeiou'
for eachIteration in vovels:
    print("Each Character:", eachIteration)


#find the average of numbers
numbersList = [1,2,3,4,5,6,7,8,9,10]
total = 0
for eachNumber in numbersList:
    total += eachNumber
print("Total:", total)
print("Average:", total/len(numbersList))

#using range() with for loop
#print(type(range(0, 10))
for num in range(0,10):
    print(num)
print("-------------------")
for num in range(0,10,2):
    print(num)
print("-------------------")
for num in range(5,10,2):
    print(num)
print("-------------------")
for num in range(10):
    print(num)

print("-------------------")
friends = ['ola','uber', 'didi', 'zoom']
for service in range(len(friends)):
    print("Service Provider (%d):" % service, friends[service])

print("--------------------------------")
#for-else loop
'''
for target_list in expression_list:
    pass
else:
    pass
'''

friends = ['ola','uber', 'didi', 'zoom']
for service in friends:
    print(service)
else:
    print("All friends done!")

print("---------------------------------------")
friends = ['ola','uber', 'didi', 'zoom']
for service in friends:
    print(service)
    if(service is 'didi'):
        print('Breaking loop! Else block will not execute!')
        break
else:
    print("All friends done!")

















