#conditions
'''
if expression:
    pass
'''
days = int(input("How may day in Jan 2020:"))
if days == 31:
    print("Correct!")
else:
    print("Un-correct!")


#if elif block!

number = input("Input anything: ")

if isinstance(number, int):
    print("It is valid integer!")
elif isinstance(number, float):
    print("It is valid float!")
elif isinstance(number, str):
    print("It is a valid string!")    
else:
    print("Help yourself. Eat something!")    

'''
>>> #one line if else statement
>>> check = 4
>>> 'It is 4' if check==4 else "It is not 4"
'It is 4'
>>> 'It is 4' if check==5 else "It is not 4"
'It is not 4'
>>>


>>> score = [21, 31, 41, 51]
>>> if 21 in score:
...     print("21 is there in score!")
...
21 is there in score!
>>> if 22 in score:
...     print("22 is there in score!")
... else:
...     print("22 is not there in score!")
...
22 is not there in score!
>>>

>>>use for, if and in to find common friends in two list!
>>> score = [21, 31, 41, 51]
>>> friends = ['ola','uber','swiggy','zoom']
>>> friends1 = ['zoom','ridez','drivez','uber']
>>> for frn in friends:
...     if frn in friends1:
...             print("Common friend: %s" %(frn))
...
Common friend: uber
Common friend: zoom
>>>

'''



