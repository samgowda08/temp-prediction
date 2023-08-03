'''Class or declaration of class will just occupy the text segment in the main memory.
Where as object occupy the stack space and called by the address
Encapsulation -> Binding up of the data and protecting it from the outer world by using the access specifier
Inheritance-> The new classes can inherit properties, methods etc., from their parent/base classes
Polymorphism-> It allows objects to take many forms depending on context
Abstraction-> Hiding complex details behind simple interfaces that represent essential features
'''
#Name of the class should start from the capital letter ex:class Person(): , class Student(object):
class Employee: 
    'Employee class used to enter the details of the Employees'
    __empName = ""  #using __ before the variable we cannot change it outside class or function where as without using __ empName we can change it
    __empId = 0      # __ is used to declare the variable privately
    countEmp = 0
 # def __init__(self,name) -> This is a constructor (self is an object for self referencing object)
    def __init__(self,name,id):
        self.__empName = name
        self.__empId = id
        Employee.countEmp += 1
    def display(self):
        print(self.__empName,self.__empId)
    def test(self):
        print("Hello")
emp1 = Employee("Sampath",1001)
emp2 = Employee("Naveen",1002)
emp3 = Employee("Anvitha",1003)
emp4 = Employee("Nisha",1004)

print(emp1, type(emp1))
emp1.test()
emp1.display()
print(Employee.countEmp)  #or
print(emp2.countEmp) #Here count can be changed by taking emp2.countName as variable and assigning the value to it
print(Employee.__doc__)
print(Employee.__class__)
print(Employee.__module__)
print(Employee.__dict__)

 

