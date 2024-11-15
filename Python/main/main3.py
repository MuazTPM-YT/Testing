List=[153,370,371,407,456,630]
List1=[]
n=len(List)
print("Original List:",List)

for i in range(0,n):
    num=List[i]
    sum=0

    while num!=0:
        rem=num%10
        pow=rem**3
        sum+=pow
        num//=10

    if sum == List[i]:
        List1.append(List[i])

print("New List:",List1)
print("Largest Number in New List:",max(List1))
print("Smallest Number in New List:",min(List1))