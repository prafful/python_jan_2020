mytuple = ()
print(mytuple)

mytuple1 = (25, 25, 45, 'hello', [45, "me too!"])
print(type(mytuple1))

tupeoftupe = ((25, 35, 45), (85, 75, 65))
print(tupeoftupe)

checkTupe = tuple({23, 45, 78})
print(checkTupe)
checkTupe = tuple([23, 45, 88])
print(checkTupe)
print(checkTupe[0])
print(checkTupe[-1])

sliceTupe = (1,2,3,4,5,6,7,8,9)
print(sliceTupe[1:])
print(sliceTupe[:4])
print(sliceTupe[-5:])

#sliceTupe[0]=0
#del sliceTupe[0]
#print(sliceTupe)

print(10 in sliceTupe)

for num in sliceTupe:
    print(num)



del sliceTupe
#print(sliceTupe)
