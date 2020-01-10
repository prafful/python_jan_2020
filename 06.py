
C:\Training\CTS\Jan 2020 Python\Examples
λ python
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #unordered colleciton of uniques and immutable values/objects

>>> #set
>>> firstSet = set("prafful daga")
>>> firstSet
{'g', 'u', 'p', 'a', 'd', 'l', ' ', 'r', 'f'}
>>> secondSet{'prafful', 'daga','chennai'}
  File "<stdin>", line 1
    secondSet{'prafful', 'daga','chennai'}
             ^
SyntaxError: invalid syntax
>>> secondSet = {'prafful', 'daga','chennai'}
>>> secondSet
{'chennai', 'prafful', 'daga'}
>>> check= {'hep', 'hep','ok'}
>>> check
{'hep', 'ok'}
>>> check.add('newone')
>>> check
{'hep', 'newone', 'ok'}
>>> check.add('newone')
>>> check
{'hep', 'newone', 'ok'}
>>> check.add('newone1')
>>> check
{'newone1', 'hep', 'newone', 'ok'}
>>> frozencheck = frozenset(check)
>>> type(check)
<class 'set'>
>>> type(frozencheck)
<class 'frozenset'>
>>> check.add(cf'')
  File "<stdin>", line 1
    check.add(cf'')
                ^
SyntaxError: invalid syntax
>>> check.add('cf')
>>> check
{'cf', 'ok', 'newone1', 'hep', 'newone'}
>>> frozencheck.add('cf')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
>>>