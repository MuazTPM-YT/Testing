# def PushNV(N):
#     for i in N:
#         for j in i:
#             if j in "AEIOUaeiou":
#                 break
#         else:
#             NoVowel.append(i)

# All=[]
# NoVowel=[]

# for i in range(5):
#     ele=input("Enter element: ")
#     All.append(ele)

# PushNV(All)
# print(All)
# print(NoVowel)

# while True:
#     if NoVowel==[]:
#         print("EmptyStack")
#         break
#     else:
#         print(NoVowel.pop(),end=' ')

# def Push3_5(N):
#     for i in N:
#         if i%5==0 or i%3==0:
#             Only3_5.append(i)

# NUM=[]
# Only3_5=[]

# for i in range(5):
#     num=int(input("Enter number: "))
#     NUM.append(num)

# Push3_5(NUM)
# print(NUM)
# print(Only3_5)

# while True:
#     if Only3_5==[]:
#         print("EmptyStack")
#         break
#     else:
#         print(Only3_5.pop(),end=' ')

# def POP_PUSH(LPop,LPush,N):
#     if N>len(LPop):
#         print("Pop not possible")
#     else:
#         for i in range(N):
#             LPush.append(LPop.pop())
#     return LPush

# LPop=[10,15,20,30]
# LPush=[]
# N=int(input("Enter N: "))

# LPush=POP_PUSH(LPop,LPush,N)
# print(LPop)
# print(LPush)

stack=[]

def Push_element(L):
    for i in L:
        if i[1]>100000:
            stack.append(i)

def Pop_element():
    if stack==[]:
        print("Stack Underflow")
    else:
        print(stack.pop())

L=[
    ["MCA",200000,3],
    ["MBA",500000,2],
    ["BA",100000,3],
]

Push_element(L)
Pop_element()