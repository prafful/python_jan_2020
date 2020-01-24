"""
Reduce
1. Works with iterable
2. It will return single value
3. Aggregator function

"""
from functools import reduce

numbers = [1,2,3,4,5]
total = reduce(lambda a,b: a*b, numbers)
print(total)

###############################
#use reduce to get max value in iterable
numbers = [51, 41, 21, 101, 54, 84]
maximum = reduce(lambda n1, n2: n1 if(n1>n2) else n2, numbers)
print(maximum)
#use reduce to get min value in iterable
numbers = [51, 41, 21, 101, 54, 84]
maximum = reduce(lambda n1, n2: n1 if(n1<n2) else n2, numbers)
print(maximum)
###########################non-lambda way#########################
#use reduce to get max value in iterable
def getLargerNumberOfTwo(n1, n2):
    return n1 if n1>n2 else n2
    """ if n1>n2:
        return n1
    else:
        return n2    
    """

numbers = [51, 41, 21, 101, 54, 84, 202]
maximum = reduce(getLargerNumberOfTwo, numbers)
print("Non Lambda way: ", maximum)
##################################################################test
#range of numbers -> range(1,5)
lastNumber =100
total = reduce(lambda a,b: a+b, range(0, lastNumber+1))
print(total)

###############################################################
# 1. Get the number >= 4 from the list -> filter
# 2. Square those numbers -> map

numbers = [1,2,3,4,5,6,7,8,9]
#1 to 3 -> [2,3,4]
#6 to 8 -> [7,8,9]
#final -> [2,3,4,7,8,9]

greater = list(filter(lambda n1: n1>=1 and n1<4, numbers))
print(greater)
square = list(map(lambda n1: n1*n1, greater))
print(square)
#all in single line
check = list(map(lambda n1: n1*n1, filter(lambda n1: n1>=1 and n1<4,numbers)))
print(check)

################################################
sum = reduce(lambda a,b: a+b  , (map(lambda n1: n1*n1, filter(lambda n1: n1>=1 and n1<4,numbers))))
print(sum)
################################################
def function1(a,b):
    return a+b

def function2(c):
    return c*c 

def function3(d):
    if d>=1 and d<4:
        return True
    else:
        return False            

sum = reduce(function1  , (map(function2, filter(function3,numbers))))
print("Function way: " , sum)








