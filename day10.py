'''
class findPrime:
    __num = 0    
    def __init__(self, num):
        self.__num = num
    def isPrime(n):
        flag = 0
        for i in range(2,(n+1)//2):
            if(n%i==0):
                flag = 1
                break
        if flag == 1:
            print("Number is not a prime")
        else:
            print("Number is a prime")

    def getDigits(self,num):
        x = self.isPrime()
        print(x)
        
x = findPrime(5) 
print(x)
x.getDigits(5)
'''
'''
class Person:
    
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        print("Master/Super/Base Class")
    def display(self):
        print(self.Name,self.Age)
class Employee:
    
    def __init__(self,id):
        self.ID = id
        print("Child/Derived class")
    def display(self):
        print(self.ID)
p = Person("sampath",22)
e = Employee(123)
e.display()
p.display()
'''
'''
class A:
    a = 0 
    b = 0 
    def __init__(self):
        self.a = 10
        self.b = 20
        print("Constructor Class A")
        print(self.a,self.b)
    def displayA(self):
        print("Disp A",self.a,self.b)
    def setValA(self,v1,v2):
        self.a = v1
        self.b = v2
    def disp(self):
        print("Hello A")
class B:
    c = 0
    d = 0
    def __init__(self):
        A.__init__(self)
        self.c = 30
        self.d = 40
        print("Constructor class B")
        print(self.c ,self.d )
    def displayB(self):
        print("Disp B",self.c,self.d)        
    def setValB(self,v1,v2):
        self.c = v1+
        self.d = v2
    def disp(self):
        print("Hello B")
#Multi Inheritance
class C(B,A):           #It is a late Binding #Class C inherits first B  and then it inherits class A
    
    def __init__(self):
        print("Class C")

        
# x = A()
# x.displayA()
# y = B()
# y.setValA(12,34)
# y.setValB(2344,55)
# y.displayB()
# y.displayA()
X = C()
X.setValA(123,33)
X.setValB(99,54)
X.displayA()
X.displayB()
X.disp()
'''
class A:
    
    def __init__(self,a,b):
        self.a = 12
        self.b = 22
        print("Class A")
    def dispA(self):
        print("class B",self.a,self.b)
class B(A):
    
    def __init__(self ,c,d):
        
        self.c = 442
        self.d = 23
        print("Class B")
    def dispB(self):
        print("Class B",self.c,self.d)
class C(B):
    
    def __init__(self,x,y):
        super().__init__()
        self.x = 3
        self.y = 32
        print("Class C")
    def dispC(self):
        print("Class C",self.x,self.y)
    def __str__(self):
        return "Hello"
c = C(10,23)
a = A(23,44)
b = B(21,33)
a.dispA()
c.dispC()
b.dispB()
c.dispA()
c.dispB()