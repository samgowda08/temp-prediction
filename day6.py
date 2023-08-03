'''
a = []
n = int(input("Enter the number: "))
for i in range(0,n+1):
    if(i%2==0):
        a.insert(i//2,i)
    else:
        a.insert((n+i)//2,i)
print(a)
'''
'''
##UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
x = 10
def func():
    y = 5
    x = x+y
    print("inside the function ",x)
func()
print("outside: ",x)
'''
'''
x=10
def outer():
    global x
    x += 15
    y = 100
    def inner():
        #x = 20
        nonlocal y
        y = y +15
        print("Inner: ",x)
        print("y: ",y)
    inner()
    print("outer: ",x)
outer()
print("Outside: ",x)
'''
'''
t1 = 'a','b','c'
print(t1,type(t1))
t2 = 'a',    #tuple with one values (at the end)
print(t2)
for i in t1:
    print(i)
print("Printing with the index value",t1[2])

t = 1,2,4
t += 5,6
print(t)
'''
'''
def isPrime(n):
    flag = 0
    for i in range(2,(n+1)//2):
        if(n%i==0):
            flag = 1
            break
    if(flag == 1):
        return False
    else:
        return True
n = int(input("Enter the number: "))
count = 0
a = []
for i in range(1,n+1):
    for j in range(i,n+1):
        if(isPrime(i) and isPrime(j)):
            if((i+j)==n):
                count += 1
                a.append([i,j])
            
print("Number of ways {}".format(count))
print(a)
'''
'''
n = list(map(int, input("Enter the unsorted array: ").split()))
num = len(n)
sum1 = int(input("Enter the sum: "))
a = []
for i in range(0,num):
    if(sum(n)==sum1):
        print("Sum Found Between {}  and {}".format((i-1),(num-1)))
        print(n)
    n.pop()
'''