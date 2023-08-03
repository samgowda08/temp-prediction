import datetime

ret = datetime.datetime.now() # today () or now()

print(ret)
print(ret.strftime("%A")) #prints the day
print(ret.strftime("%a")) #print the day in shortform
print(ret.strftime("%B"))   #print the month
print(ret.strftime("%D"))  #print the date month/date/year
print(ret.strftime("%I:%M:%S %p")) #print (hours:minutes:seconfs  AM/PM)
print(ret.strftime("%F")) #prints year-month-day
print(ret.strftime("%G"))   #prints the year

ret1 = datetime.datetime(2002,8,8)
print(ret1.strftime("%A")) #prints the day
print(ret1.strftime("%B")) #prints the month
