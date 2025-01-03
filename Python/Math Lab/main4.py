from sympy import *

x = Symbol('x')

y = Function('y')(x)
y1 = diff(y,x)

DE = Eq(y1 + y*tan(x) - y**3*sec(x), 0)
GS = dsolve(DE)

print(GS)