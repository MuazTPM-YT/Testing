A=[[2,4],[6,8]]
B=[[1,3],[5,7]]

C=[[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j]+=A[i][k]*B[k][j]

for i in C:
    print(i)