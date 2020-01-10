
C:\Training\CTS\Jan 2020 Python\Examples
λ python
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> firstDict = {'key':'value', 'monday':1, 'tuesday':2, 'thursday':4}
>>> type(firstDict)
<class 'dict'>
>>> firstDict[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> firstDict['key']
'value'
>>> firstDict['monday']
1
>>> firstDict['thursday']
4
>>> firstDict['thursday1']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'thursday1'
>>> firstDict['thursday']=3
>>> firstDict
{'key': 'value', 'monday': 1, 'tuesday': 2, 'thursday': 3}
>>> firstDict.update({'wednesday':4})
>>> firstDict
{'key': 'value', 'monday': 1, 'tuesday': 2, 'thursday': 3, 'wednesday': 4}
>>> firstDict['wednesday']=
  File "<stdin>", line 1
    firstDict['wednesday']=
                          ^
SyntaxError: invalid syntax
>>> firstDict['wednesday']=3
>>> firstDict
{'key': 'value', 'monday': 1, 'tuesday': 2, 'thursday': 3, 'wednesday': 3}
>>> firstDict.del('thursday')
  File "<stdin>", line 1
    firstDict.del('thursday')
              ^
SyntaxError: invalid syntax
>>> del firstDict('thursday')
  File "<stdin>", line 1
SyntaxError: cannot delete function call
>>> del firstDict['thursday']
>>> firstDict
{'key': 'value', 'monday': 1, 'tuesday': 2, 'wednesday': 3}
>>>

