# Find the ROC of the curve, r = 4(1+cos(theta)) at theta = pi/2

from sympy import *

theta = symbols('theta')

r = 4*(1+cos(theta))

r1 = diff(r,theta)
r2 = diff(r1,theta)

rho = ((r**2 + r1**2)**1.5)/(r**2 + 2*r1**2 - r2*r)
rho1 = rho.subs(theta, pi/2)

print(f"ROC: {simplify(rho1):0.3f}")