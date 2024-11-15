import csv

f=open("Python/school/practicals/assets/file.csv",'w')
w=csv.writer(f)
w.writerow(["UserID", "Password"])

while True:
    userid=input("User ID: ")
    password=input("Password: ")
    data=[userid, password]
    w.writerow(data)

    opt=input("Do you want to add more? (y/n): ").lower()
    if opt=="n":
        print("Accounts Added!")
        f.close()
        break

f=open("Python/school/practicals/assets/file.csv",'r')
r=csv.reader(f)
found=0

search=input("Search by UserID: ")

for i in r:
    if i==[]:
        pass
    elif i[0]==search:
        print(f"Searched Account: {i}")
        found=1
    else:
        pass

f.close()

if found==0:
    print("UserID is not Found")