S='LOST'
L=[10,21,33,4]
D={}
for i in range(len(S)):
  if i%2==0:
    D[L.pop()]=S[i]
  else:
    D[L.pop()]=i+3
  
for k,v in D.items():
  print(k,v,sep="*")