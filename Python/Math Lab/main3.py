from sympy import *

x,a,b,c,d = symbols('x,a,b,c,d')

f = ((a**x + b**x + c**x + d**x)/4)**(1/x)

L = Limit(f,x,0).doit()

print(L)