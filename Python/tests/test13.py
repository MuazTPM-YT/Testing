from time import sleep
for x in range(0,3):  
    b = "Loading" + "." * x
    print (b, end="\r")
    sleep(1)