import pickle

def create():
    f=open("Python/school/practicals/assets/file.dat", 'ab')

    while True:
        rollno=int(input("Roll No: "))
        name=input("Name: ")
        L=[rollno, name]
        pickle.dump(L,f)
        
        opt=input("Do you want to add more? (y/n): ")
        if opt.lower()=="n":
            print("Details Added!")
            f.close()
            break

def search():
    f=open("Python/school/practicals/assets/file.dat", 'rb')
    search=int(input("Search by Roll No: "))
    found=0
    try:
        while True:
            r=pickle.load(f)
            if r[0]==search:
                print(f"Searched Details: {r}")
                found=1
                break
    except:
        f.close()

    if found==0:
        print("Roll No. is not Found")

create()
search()