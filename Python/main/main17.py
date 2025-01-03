# # def findClosestNumber(nums):
# #     close = abs(nums[0]-0)
# #     acc=0

# #     for i in range(1,len(nums)):
# #         if abs(nums[i]-0) < close:
# #             close = abs(nums[i]-0)
# #             acc=i

# #     if nums[acc]<0 and nums[acc+1]==abs(nums[acc+1]):
# #         return nums[acc+1]
# #     else:
# #         return nums[acc]

# # # nums = [-4,-2,1,4,8]
# # nums = [2,-1,1]

# # print(findClosestNumber(nums))

# # def hasDuplicate(nums):
# #     if len(set(nums)) < len(nums):
# #         return True
# #     else:
# #         return False

# # nums = [1, 2, 3, 3]

# # print(hasDuplicate(nums))

# # s = "racecar"
# # t = "carrace"

# # s="bbcc"
# # t="ccbc"

# # s = list(s)
# # print(s)


# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None

# laptop_on = True
# user = "Muaz"

# if laptop_on == True:
#     if user == "Muaz":
#         print("Hello Muaz!")
#     else:
#         print("Hello Random Person!")
# else:
#     print("Goodbye World!")

from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x,y=symbols('x,y')
sol=solve([2*x+y-7, 3*x-y-3],[x,y])
p=sol[x]
q=sol[y]

print(f"Point of Intersection is A({p},{q})\n")
x=np.arange(-10,10,0.001)

y1=7-2*x
y2=3*x-3

plt.plot(x,y1,'r')
plt.plot(x,y2,'g')
plt.plot(p,q,marker='o')

plt.show()