
C:\Training\CTS\Jan 2020 Python\Examples
λ python
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> firstTupe = ()
>>> firstTupe
()
>>> type(firstTupe)
<class 'tuple'>
>>> firstTupe = (8, 5, 88.8, 7)
>>> firstTupe
(8, 5, 88.8, 7)
>>> onemoreTupe = ('Help','Tuple')
>>> checkThis = (firstTupe, onemoreTupe)
>>> checkThis
((8, 5, 88.8, 7), ('Help', 'Tuple'))
>>> #nestedTuple
>>> firstTupe
(8, 5, 88.8, 7)
>>> firstTupe[1:]
(5, 88.8, 7)
>>> firstTupe[1:3]
(5, 88.8)
>>> firstTupe[1]
5
>>> firstTupe[1] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> firstTupe = ()
>>> firstTupe
()
>>> firstTupe = ()
>>>
>>>