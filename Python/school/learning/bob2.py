# def func():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.readlines()

#     for i in r:
#         if 'y' in i.lower():
#             print(i, end='')
#     f.close()
# func()

# def RevString():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.read()
#     L=r.split()
#     for i in range(len(L)):
#         if L[i][0]=='O':
#             L[i]=L[i][::-1]
#     print(' '.join(L))
#     f.close()
# RevString()

# def LongLines():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.readlines()
#     for i in r:
#         if len(i.split())>=10:
#             print(i,end='')
#     f.close()
# LongLines()

# def count_Dwords():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.read()
#     count=0
#     for i in r:
#         if i.isdigit():
#             count+=1
#     print(f"Number of words ending with a digit are {count}")
#     f.close()
# count_Dwords()

# def ChangeGender():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     w=f.read()
#     r=w.split()
#     for i in range(len(r)):
#         if r[i]=='he':
#             r[i]='she'
#     print(' '.join(r))
#     f.close()
# ChangeGender()

# def Count_Line():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.readlines()
#     print(f"Total number of lines: {len(r)}")
#     f.close()
# Count_Line()

# def Show_words():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.read()
#     print(r.upper())
#     f.close()
# Show_words()

# def Show_words():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.readlines()
#     for i in r:
#         if len(i.split())==5:
#             print(i,end='')
#     f.close()
# Show_words()

# def COUNTLINES():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     w=f.readlines()
#     count=0
#     for i in w:
#         if i[0] not in 'AEIOUaeiou':
#             count+=1
#     print(f"The number of lines not starting with any vowel - {count}")
#     f.close()
# COUNTLINES()

# def ETCount():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.read()
#     e=t=0
#     for i in r:
#         if i.lower()=='t':
#             t+=1
#         if i.lower()=='e':
#             e+=1
#     print(f"The number of E or e: {e}")
#     print(f"The number of T or t: {t}")
#     f.close()
# ETCount()

# def func():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.read()
#     c=0
#     for i in r.split():
#         if i=='Me' or i=='My':
#             c+=1
#     print(f"Count of Me/My in file: {c}")
#     f.close()
# func()

# def AMCount():
#     f=open("Python/school/practicals/assets/file.txt",'r')
#     r=f.read()
#     a=m=0
#     for i in r:
#         if i.lower()=='a':
#             a+=1
#         if i.lower()=='m':
#             m+=1
#     print(f"A or a: {a}")
#     print(f"M or m: {m}")
#     f.close()
# AMCount()