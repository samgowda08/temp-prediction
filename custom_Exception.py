class InvalidAgeException(Exception):
    pass
try:
    age = int(input("Enter the age: "))
    if age<0:
        raise InvalidAgeException
    else:
        print("Eligible")
except InvalidAgeException as i:
    print("Invalid Age: ",i)