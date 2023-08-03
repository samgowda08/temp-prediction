'''
from collections import namedtuple

Emp = namedtuple('Emp',['ename','eage','eid'])

e1 = Emp("Sampath",'20','123')
print(e1)
print(e1[2])
print(e1.ename)
print(sorted(e1))
'''