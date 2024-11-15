# def COUNTNOW(REGIONS):
#     for i in REGIONS:
#         if len(i)<=5:
#             print(i)

# L=["GOA","NEW DELHI","DAMAN","CHENNAI","BANGALORE"]
# COUNTNOW(L)

# def FindOut(Names,HisName):
#     for i in range(len(Names)):
#         if Names[i]==HisName:
#             print(f"{HisName} at {i}")

# Names=["Arun","Raj","Tarun","Kanika"]
# HisName="Tarun"

# FindOut(Names,HisName)

# def TenTimesEven(VALUES):
#     sum1=0
#     for i in VALUES:
#         if i%2==0:
#             sum1+=(i*10)
#     print(f"Even Sum: {120}")

# Nums=[5,2,3,6,3,4]
# TenTimesEven(Nums)

# def EndingA(Names):
#     for i in Names:
#         if i[-1]=='A':
#             print(i)

# Names=["JAYA","KAREEM","TARUNA","LOVISH"]
# EndingA(Names)

# def Swapper(Numbers):
#     SL=Numbers
#     for i in range(len(Numbers)//2):
#         SL[i],SL[i+3]=SL[i+3],SL[i]
#     return SL

# L=[35,67,89,23,12,45]
# print(Swapper(L))

# def LShift(Arr,n):
#     for i in range(n):
#         x=Arr[0]
#         for j in range(len(Arr)-1):
#             Arr[j]=Arr[j+1]
#         Arr[len(L)-1]=x
#     return Arr

# L=[10,20,30,40,12,11]
# n=2
# print(LShift(L,n))

# def search_replace(L,n):
#     for i in range(len(L)):
#         if L[i]==n:
#             L[i]=0

#     print(L)
    
# L=[10,20,30,10,40]
# n=10
# search_replace(L,n)