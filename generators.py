'''
Syntax: 
    
    def funcName()
        yield sts
'''
''''
def fName():
    for i in range(10):
        yield i*i
g1 = fName()
print(g1,type(g1))
for i in g1:
    print(i)
'''
