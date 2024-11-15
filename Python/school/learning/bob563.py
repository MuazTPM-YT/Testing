import csv

# def AddDevice():
#     f=open("Python/school/practicals/assets/file.csv",'w')
#     w=csv.writer(f)

#     while True:
#         P_id=input("Enter P Id: ")
#         P_name=input("Enter P Name: ")
#         Price=int(input("Enter Price: "))
#         data=[P_id,P_name,Price]
#         w.writerow(data)

#         opt=input("Do you want to add more? (y/n): ").lower()
#         if opt=="n":
#             print("Accounts Added!")
#             f.close()
#             break

# def Count_Device():
#     f=open("Python/school/practicals/assets/file.csv",'r')
#     r=csv.reader(f)
#     c=0
#     for i in r:
#         if i==[]:
#             pass
#         elif int(i[2])<1000:
#             print(i)
#             c+=1
#         else:
#             pass
#     print(f"No: {c}")

# AddDevice()
# Count_Device()

# def COURIER_ADD():
#     f=open("Python/school/practicals/assets/file.csv",'a', newline='\n')
#     w=csv.writer(f)

#     while True:
#         cid=input("Enter CID: ")
#         s_name=input("Enter SNAME: ")
#         Source=input("Enter SOURCE: ")
#         destination=input("Enter DEST: ")
#         data=[cid,s_name,Source,destination]
#         w.writerow(data)

#         opt=input("Do you want to add more? (y/n): ").lower()
#         if opt=="n":
#             print("Accounts Added!")
#             f.close()
#             break

# def COURIER_SEARCH():
#     f=open("Python/school/practicals/assets/file.csv",'r')
#     r=csv.reader(f)
#     dest_search=input("Enter destination to search: ")
#     for i in r:
#         if i[3]==dest_search:
#             print(i)

# COURIER_ADD()
# COURIER_SEARCH()