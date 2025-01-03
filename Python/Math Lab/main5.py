from sympy import *

x = Symbol('x')
f = sin(x) + cos(x)

df1 = diff(f,x)
df2 = diff(df1,x)
df3 = diff(df2,x)

f = lambdify(x,f)
f1 = lambdify(x,df1)
f2 = lambdify(x,df2)
f3 = lambdify(x,df3)

f = f(0) + x * f1(0) + (x**2/2) * f2(0) + (x**3/6) * f3(0)

print(simplify(f))