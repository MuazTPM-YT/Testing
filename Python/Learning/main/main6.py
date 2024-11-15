# sum = 0
# for i in range(1,11):
#     if i%2==0:
#         sum+=i
# print(sum)

# n = 5
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# for i in range(2,7):
#     for j in range(1,i):
#         print(j,end=' ')
#     print()

# n = 5
# n1, n2 = 0, 1
# count = 0

# if n <= 0:
#    print("It must be positive")

# elif n == 1:
#    print(f"Fibonacci sequence upto {n}:")
#    print(n1)
   
# else:
#    print("Fibonacci sequence:")
#    while count < n:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1

# n = 1
# for i in range(5,0,-1):
#     print(" "*n,end="")
#     print("*"*i)
#     n+=1

# 1)
students = [["Muaz",True],["John",True],["Sam",False],["Lily",True],["Terry",True],["Timmy",True]]
age = [18,24,21,13,33,31]

# 2)
print(f"Number of students: {len(students)}")

# 3)
print(students[0])
print(students[-1])

# 4)
if students[2][1]:
    print(f"{students[2][0]} is present")
else:
    print(f"{students[2][0]} is absent")

# 5)
for i in range(len(students)):
    print(students[i])

# 6)
i = 0
while i<len(students):
    print(students[i])
    i+=1

# 7)
students[2][0] = "Brock"
print(students)

# 8)
students.append(["George",True])
print(students)

# 9)
students.extend(age)
print(students)

# 10)
students.remove(["Sam",False])
students.remove(["Terry",True])
print(students)