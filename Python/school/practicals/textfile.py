f=open("Python/school/practicals/assets/file.txt",'r')
c=f.read()
vc=cc=uc=lc=0

for x in c:
    if x.isalpha():
        if x.lower() in 'aeiou':
            vc+=1
        else:
            cc+=1
        if x.isupper():
            uc+=1
        else:
            lc+=1

f.close()

print(f"Vowels: {vc}")
print(f"Consonants: {cc}")
print(f"Uppercase: {uc}")
print(f"Lowercase: {lc}")