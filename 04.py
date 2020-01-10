
C:\Training\CTS\Jan 2020 Python\Examples
λ lists
'lists' is not recognized as an internal or external command,
operable program or batch file.

C:\Training\CTS\Jan 2020 Python\Examples
λ python
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> mixeditems = [False, 1, 8.88, 'Python']
>>> mixeditems
[False, 1, 8.88, 'Python']
>>> type(mixeditems)
<class 'list'>
>>> mixeditems[1]
1
>>> mixeditems[3]
'Python'
>>> id(mixeditems)
50337896
>>> mixeditems[0:1]
[False]
>>> mixeditems[0:2]
[False, 1]
>>> mixeditems[1:3]
[1, 8.88]
>>> mixeditems[1:4]
[1, 8.88, 'Python']
>>> mixeditems[:-1]
[False, 1, 8.88]
>>> mixeditems[-2:-1]
[8.88]
>>> mixeditems[-1:]
['Python']
>>> for item in mixeditems:
...     print(item)
...
False
1
8.88
Python
>>> mixeditems
[False, 1, 8.88, 'Python']
>>> twoDimension = [[1,2,3], [4,5,6], [7,8,9]]
>>> twoDimension
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> twoDimension[0]
[1, 2, 3]
>>> twoDimension[1]
[4, 5, 6]
>>> twoDimension[2]
[7, 8, 9]
>>> for itemout in twoDimension:
...     print(itemout)
...
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
>>> for itemout in twoDimension:
...     for itemin in itemout:
...             print(itemin)
...
1
2
3
4
5
6
7
8
9
>>>