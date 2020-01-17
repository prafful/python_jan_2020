#{}.format(parameter)
#how do you want to format . what do  you want to format
print('{}'.format('format this string'))
print('{} alien {}'.format("Hello", "Charlie"))
fname = "Hello"
lname = "Charlie"
print('{} . {}'.format(fname, lname))

#using format to work with strings
print(format("prafful", ">20s"))
#             prafful
print(format("prafful", "<20s"))
#prafful
#using format to work with strings
print(format("prafful", "$>20s"))
#$$$$$$$$$$$$$prafful
print(format("prafful", "$<20s"))
#prafful$$$$$$$$$$$$$
print(format("prafful", "$^20s"))
#$$$$$$prafful$$$$$$$

#format integers
print("My score is {}".format(88))
print("My salary is {}".format(8888888))
print("My salary is {:,}".format(8888888))
print("My score is {:5}".format(88))
print("My salary is {:20,}".format(8888888))
print("My score is {:@>5}".format(88))
print("My score is {:@<5}".format(88))
print("My score is {:@^5}".format(88))
print("My salary is {:@>20,}".format(8888888))
print("My salary is {:@<20,}".format(8888888))
print("My salary is {:@^20,}".format(8888888))

#formatting the output as binary number
num = 10
print('{0:b}'.format(num))
num = 0
while(num<=5):
    print('{0:b}'.format(num))
    num+=1
print("-----------------------------")    
num = 0
while(num<=20):
    print('{0:o}'.format(num))
    num+=1    
print("-----------------------------")        
num = 0
while(num<=20):
    print('{0:x}'.format(num))
    num+=1

#floating points
print("-------------------------")
print('{0:f}'.format(1.584642145))
print('{0:.4f}'.format(1.584642145))
print('{0:.2f}'.format(1.584642145))

import math
print(math.floor(12.5848))
print(math.ceil(12.5848))

#use format to access list item
language = ['Python', 'Flask','Django','Express']
print("I love to work with", language[3])
print("I love to work with {0[3]}".format(language))

salary ={"oli":8898, "mok":8745}
print("Oli's pay: {0[oli]} \nMok's pay: {0[mok]}".format(salary))













