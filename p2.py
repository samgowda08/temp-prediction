import re

phno = "91-99999-88888 # this is Phone Number"

num = re.sub(r'#.*$',"",phno)
print(num, type(num))
num = re.sub(r'-.*$',"",num)
print(num)
num = re.sub(r'\D',"",phno)
print(num)