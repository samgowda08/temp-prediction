import re

#re.match(patter,string, flags =0)
str1 = "Dogs are barking and they are loyal"

matchO = re.match(r'(.*) are (.*?) . *', str1,re.M)

if matchO:
    print("group: ", matchO.group())
    print("group: ", matchO.group(2))
else:
    print("no match")   
