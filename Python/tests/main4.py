from time import time
x=int(input("Enter the number: "))
t0=time()
factor = 0
for i in range(2,x):
    if x%i==0:
        factor += 1
if factor == 0:
    print(x,"is a prime number")
else:
    print(x,"is a composite number")
t1=time()
print(f"Time required: {t1-t0}")