# import matplotlib.pyplot as plt
# import numpy as np

# plt.axes(projection='polar')
# r=3
# rads=np.arange(0,(2*np.pi),0.01)

# for i in rads:
#     plt.polar(i,r,'b.')

# plt.show()

# from pylab import *
# import numpy as np

# theta = linspace(0,(2*np.pi),1000)

# x = 5*cos(theta)
# y = 5*sin(theta)
# r = sqrt(x**2 + y**2)

# polar(theta,r,'r-')
# show()

# from pylab import *
# import numpy as np

# theta = linspace(0,(2*np.pi),1000)
# r1 = 5+5*cos(theta)
# polar(theta,r1,'b')

# show()

from pylab import *
import numpy as np

theta = linspace(0,(2*np.pi),1000)

r1 = 5+5*cos(theta)
r2 = 5-5*cos(theta)
r3 = 5+5*sin(theta)
r4 = 5-5*sin(theta)

polar(theta,r1,'r')
polar(theta,r2,'g')
polar(theta,r3,'b')
polar(theta,r4,'k')

show()