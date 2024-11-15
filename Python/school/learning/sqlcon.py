import csv

def create():
    f=open('Python/school/learning/assets/emp.csv','w',newline='')
    w=csv.writer(f)
    while True:
        rollno=int(input("Enter employee number: "))
        name=input("Enter employee name: ")
        marks=int(input("Enter employee salary: "))
        l=[rollno,name,marks]
        w.writerow(l)
        opt=input("Do you want to continue (y/n)?: ")
        if opt=='n':
            break
    f.close()

def update():
    f=open('Python/school/learning/assets/emp.csv','r',newline='\r\n')
    n=int(input("Enter the employee number to search: "))
    found=0
    row=csv.reader(f)
    for data in row:
        if data[0]==str(n):
            print("\nEmployee Details are:")
            print("=======================")
            print("Name:",data[1])
            print("Salary:",data[2])
            print("=======================")
            found=1
            break

    if found==0:
        print("The searched employee no is not found")

    f.close()

create()
update()
