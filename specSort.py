# sorted (iterable , key  , reverse)
# sorted will convert into list
list = [3,4,1,2,4 ,5,6]
sList = sorted(list)
print(sList)
print(sorted("Python"))     #prints according to the ASCII value (ASCII value of Capital letter is smaller than small letter)
t = ('P','y','t','h','o','n') #Tupel is immutable so after sorting it will be in list
print(sorted(t))

d1 = { 'c':5,'b':2,'d':3,'a':1}
print(sorted(d1))
