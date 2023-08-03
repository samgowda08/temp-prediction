n = int(input("Enter the number: "))
num = str(n)
if(n<0):
    x = int(num[:0:-1])
    print("-",x,type(x))
else:
    x = int(num[::-1])
    print(x,type(x))