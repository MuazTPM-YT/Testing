import time

i = 0
space = " "

while True:
    while i<=10:
        print(f"{space*i}")
        i+=1
        time.sleep(0.01666)

    while i>1:
        print(f"{space*i}")
        i-=1
        time.sleep(0.01666)