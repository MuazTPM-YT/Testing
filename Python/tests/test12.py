list1 = []
n = int(input("Enter the number of students: "))
for i in range(0,n):
    m = float(input(f"Enter the marks of the student {i+1}: "))
    list1.append(m)
    s = sum(list1)/n
print(f"Average marks of {n} students is: {s}")