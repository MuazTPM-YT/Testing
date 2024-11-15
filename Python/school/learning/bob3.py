import pickle

# def WRITEREC():
#     f=open("Python/school/practicals/assets/file.dat", 'wb')
#     while True:
#         i_d=input("Enter ID: ")
#         name=input("Enter Name: ")
#         price=int(input("Enter Price: "))
#         data=[i_d,name,price]
#         pickle.dump(data,f)
#         opt=input("You want to add more? (y/n): ").lower()
#         if opt=='n':
#             f.close()
#             break

# def SHOWHIGH():
#     f=open("Python/school/practicals/assets/file.dat", 'rb')
#     try:
#         while True:
#             r=pickle.load(f)
#             if r[2]>500:
#                 print(r)
#     except:
#         f.close()

# WRITEREC()
# SHOWHIGH()

# def CreateFile():
#     f=open("Python/school/practicals/assets/file.dat", 'wb')
#     while True:
#         BookNo=input("Enter Book No: ")
#         Book_Name=input("Enter Book Name: ")
#         Author=input("Enter Author: ")
#         Price=int(input("Enter Price: "))
#         data=[BookNo,Book_Name,Author,Price]
#         pickle.dump(data,f)
#         opt=input("You want to add more? (y/n): ").lower()
#         if opt=='n':
#             f.close()
#             break

# def CountRec(Author):
#     f=open("Python/school/practicals/assets/file.dat", 'rb')
#     c=0
#     try:
#         while True:
#             r=pickle.load(f)
#             if Author==r[2]:
#                 c+=1
#     except:
#         f.close()
#     print(f"Number of books by {Author}: {c}")

# CreateFile()
# Author=input("Enter Author to Count: ")
# CountRec(Author)

# def CreateFile():
#     f=open("Python/school/practicals/assets/file.dat", 'wb')
#     while True:
#         admission_number=input("Enter Admission No: ")
#         Name=input("Enter Name: ")
#         Percentage=int(input("Enter Percentage: "))
#         data=[admission_number,Name,Percentage]
#         pickle.dump(data,f)
#         opt=input("You want to add more? (y/n): ").lower()
#         if opt=='n':
#             f.close()
#             break

# def CountRec():
#     f=open("Python/school/practicals/assets/file.dat", 'rb')
#     c=0
#     try:
#         while True:
#             r=pickle.load(f)
#             if r[2]>75:
#                 print(r)
#                 c+=1
#     except:
#         f.close()
#     print(f"Number of students scoring above 75%: {c}")

# CreateFile()
# CountRec()

# def CreateFile():
#     f=open("Python/school/practicals/assets/file.dat", 'wb')
#     while True:
#         SportsName=input("Enter SportsName: ")
#         TeamName=input("Enter TeamName: ")
#         No_Players=input("Enter No_Players: ")
#         data=[SportsName,TeamName,No_Players]
#         pickle.dump(data,f)
#         opt=input("You want to add more? (y/n): ").lower()
#         if opt=='n':
#             f.close()
#             break

# def copyData():
#     f1=open("Python/school/practicals/assets/file.dat", 'rb')
#     f2=open("Python/school/practicals/assets/file2.dat", 'wb+')
#     c=0
#     try:
#         while True:
#             r=pickle.load(f1)
#             if r[0]=="Basket Ball":
#                 pickle.dump(r,f2)
#                 c+=1
#     except:
#         f1.close()
#         f2.close()

#     return c

# CreateFile()
# print(copyData())