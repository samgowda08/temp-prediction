'''
l = []
for i in range(1,11):
    l.append(i*i)
print(l)
'''
'''
# listVar = [resultValue Expression]
l1 = [ i*i for i in range(1,11)]
print(l1)
l2 = list(range(5))
print(l2)
'''
'''
str1 = "This is a Python Programming Class"
count = 0 
for i in str1:
    if i.lower() in ['a','e','i','o','u']:
        count +=1
print(count)
######
lV = [i for i in str1 if i.lower() in ['a','e','i','o','u']]    # if there is IF statement it should be after the for loop
print(lV,len(lV))
'''
'''
l3 = [i for i in range(1,101) if i%2==0] + [i for i in range(1,101) if i%2!=0]
print(l3)
'''
'''
l4 = []
def f1(n):
    return(n*n)+25
for i in range(1,11):
    l4.append(f1(i))
print(l4)

f2 = lambda n: (n*n)+25
l5 = [f2(i) for i in range(1,11)]
print(l5)

l6 = [(lambda num: (num*num)+25)(num) for num in range(1,11)]
print(l6)
'''
'''
n = int(input("Enter the number: "))
l7=["{}X{}={}".format(n,i,n*i) for i in range(1,11)] 
print(l7)
####
l8 = ["{}X{}={}".format(i,j,i*j) for i in range(2,6) for j in range(1,11)]
print(l8)
'''
