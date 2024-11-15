NList=[
    ["NewYork", "USA", 11734],
    ["Naypidaw", "Myanmar", 3219],
    ["Dubai", "UAE", 2194],
    ["London", "England", 6693],
    ["Gangtok", "India", 1580],
    ["Colombo", "Sri Lanka", 3405]
]

stack=[]

def notEmpty():
    if stack!=[]:
        return True
    else:
        return False

def Push(NList):
    for i in NList:
        if i[1]!="India" and i[2]<3500:
            L=[i[0],i[1]]
            stack.append(L)

def Pop():
    while notEmpty():
        item=stack.pop()
        print(item)

    print("Stack empty")

Push(NList)
Pop()

# INSERT INTO OPD VALUES('R130', 'Naman', 30, 'ENT', '2023-07-10', 700, 'M');
# UPDATE OPD SET Charges=Charges+200 WHERE Department='ENT';
#
