f=open("Python/assets/main.txt","r")
r=f.readlines()

for i in r:
    w=i.split()
    for j in w:
        print(j,end="#")

f.close()