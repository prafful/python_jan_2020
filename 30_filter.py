"""
Filter

It works on iterable
It will work with two parameters
1. Function/Lambda
2. Iterables

A. Function/Lambda will evalaute for each item in iterable one by one!
B. It return list of items for which lambda/function evaluates to TRUE!

"""
numbers = [12,22,33,44,56,68,70,42,63]
selected = filter(lambda a: a>40, numbers)
print(list(selected))

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
vowels = ['a','e','i','o','u']

selected = list(filter(lambda a: a in vowels , alphabets))
print(selected)
##########################non-lambda way###########################

def findVowelsInList(a):
    return a in vowels


selected = list(filter(findVowelsInList , alphabets))
print("Function way: ", selected)

