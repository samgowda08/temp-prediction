import time

print("Implementation of sleep")
for i in range(1,11):
    print(i)
    time.sleep(0.1)
    print("After Sleep")
localtime1 = time.localtime()
ret = time.strftime("%I:%M:%S %p",localtime1)
print(ret)