#calling same function within the function

#factorial example

def calculateFactorial(num):
    if num != 1:
        return num * calculateFactorial(num-1)
    else:
        return 1    


number = int(input("Input Number: "))
print(calculateFactorial(number))

'''
 python 21_recursion.py
Input Number: 1000
Traceback (most recent call last):
  File "21_recursion.py", line 13, in <module>
    print(calculateFactorial(number))
  File "21_recursion.py", line 7, in calculateFactorial
    return num * calculateFactorial(num-1)
  File "21_recursion.py", line 7, in calculateFactorial
    return num * calculateFactorial(num-1)
  File "21_recursion.py", line 7, in calculateFactorial
    return num * calculateFactorial(num-1)
  [Previous line repeated 995 more times]
  File "21_recursion.py", line 6, in calculateFactorial
    if num != 1:
RecursionError: maximum recursion depth exceeded in comparison

'''

