import re

pattern  = r'123'
str1 = "123xxyyzz"
ret = re.match(pattern,str1)
print(ret.group())

ret = re.match(r"123","abc123xyz")

if ret is None:
    print("not found")
else:
    print(ret.group())
    
ret = re.search(r"12","abc123xyz")
    
if ret is None:
    print("not found")
else:
    print(ret.group())    
    
ret = re.search(r'123$',"abcde123z")

print(ret.group(0))