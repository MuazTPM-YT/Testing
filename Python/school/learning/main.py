f = open("Python/school/learning/assets/main.txt")
c=f.read()
vc=0
cc=0
lc=0
uc=0

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
print(f"Lowercase: {lc}")
print(f"Uppercase: {uc}")