import time
n = input("Type your number here: ")

for i in range(0,11):
    xy = int(n)*int(i)
    print(xy)
    time.sleep(1)