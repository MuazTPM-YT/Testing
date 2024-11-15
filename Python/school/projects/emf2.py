from math import sin

l=[]

for t in range(0,31):
    w=105
    N=500
    B=1.5
    A=2
    emf= -(N*B*A*w*sin(w*t))
    print(f"EMF Produced in {t} seconds: {(2*emf)/1000}")
    l.append(abs((2*emf)/1000))

print(f"Average EMF Produced: {sum(l)/len(l)}")