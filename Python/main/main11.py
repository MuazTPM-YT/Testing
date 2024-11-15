matrix=[]

row=int(input("Enter a row: "))
column=int(input("Enter a column: "))

if row==column:
    for x in range(1,row+1):
        for y in range(1,column+1):
            element=int(input(f"Enter a{x,y}: "))
            matrix.append(element)
            
    for i in range(0,len(matrix)-2, 3):
        print(f"[{matrix[i]} {matrix[i+1]} {matrix[i+2]}]")

else:
    print("It must be a square matrix")