'''
keys1 = ['a','b','c','d','e']
values1 = [1,2,3,4]
# print(zip(keys1,values1))
d1 = {}
for i,j in zip(keys1,values1):
    print("key:",i,"value:",j)
    d1[i]=j
print(d1)
d2 = {k:v for (k,v) in zip(keys1,values1)} #dictionary comphrension
print(d2)
d3 = {i:i*i for i in range(1,11)}   #str(i) used to convert the given into string
print(d3)
'''