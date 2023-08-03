'''
l = [1,2,3,4,5,6,7,8]
k = 3
rL = []
count = 0
i = 0
while i<len(l):
    t = l[count: count+k]
    t.reverse()
    rL += t
    i += k
    count += k
print(rL)
'''
'''
l = [1,3,5,7,9]
a = 0
for i in l:
    a += i**2
print(a)
'''
'''
#functools.reduce(function,iterable_obj)
import functools
l = [1,3,5,7,9]
sum = functools.reduce(lambda x,y:x+y ,map(lambda x: x*x,l))
print(sum)
'''
'''
list2= ['Python','visual','code','peter','jones','student']
x = frozenset(list2)
print(x,type(x))
print(x)
'''