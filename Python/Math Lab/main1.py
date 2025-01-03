# find the angle between the curves r=4*cos(t) and r=5*sin(t)

from sympy import *
import math

theta = symbols('theta')

r1 = 4*(1+cos(theta))
r2 = 5*(1-cos(theta))

dr1 = diff(r1,theta)
dr2 = diff(r2,theta)

tanphi1 = r1/dr1
tanphi2 = r1/dr2

q = solve(r1-r2, theta)

w1 = tanphi1.subs({theta: float(q[0])})
w2 = tanphi2.subs({theta: float(q[0])})

phi1 = atan(w1)
phi2 = atan(w2)

angle = abs(phi1 - phi2)

print(f"Angle: {math.degrees(angle):0.3f} degrees")
print(f"Angle: {angle:0.3f} radians")