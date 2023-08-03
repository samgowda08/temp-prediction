def outF():
    def inF():
        print("Inside the function")
    inF()
    print("Outside the funciton")
    return (inF)
outF() #You cannot call the inFunction with the help of outFunction only you can call the inFunction
test1 = outF #variable is converted into a function
# print(test1)
# print(test1.__name__)
test1()

