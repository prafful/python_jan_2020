#lambda functions
"""
no-named/anonymous light-weight function. 
no need to use def keywork
inline functions

"""
num1 = 4
num2 = 5
myadd = lambda a: a + a
print(myadd(num1))

mymultiply = lambda b: b * b
print(mymultiply(num1))


myadd = lambda a,b: a + b
print(myadd(num1, num2))

lambdaList = [lambda a: a**2, lambda a,b: a*b, lambda a,b: a+b]
value1 = lambdaList[0](10)
value2 = lambdaList[1](7,5)
value3 = lambdaList[2](7,5)
print(value1, " ", value2, " ", value3)

#map -> will work only on collection
#    -> it will return the list created by lambda function (parameter of map)

messages = ["Help", "Run", "Walk", "Eat", "Speak"]

mapdone = map(lambda a: '@'+a+'@', messages)

print(list(mapdone))


mapdone = map(lambda a: a.upper(), messages)

print(list(mapdone))