stack=[]

def Push(item):
    stack.append(item)

def Pop():  
    if stack==[]:
        print("Stack Underflow")
    else:
        x=stack.pop()
        return x

def Peek():
    if stack==[]:
        print("Stack is Empty")
    else:
        print(f"Top: {stack[-1]}")

def Display():
    if stack==[]:
        print("Stack is Empty")
    else:
        print(f"Top: {stack[-1]}")
        for i in range(len(stack)-2,-1,-1):
            print(stack[i])

while True:
    print("Stack Operations")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")

    opt=int(input("Enter your choice: "))

    if opt==1:
        item=int(input("Number: "))
        Push(item)

    elif opt==2:
        print(f"Successfully Deleted: {Pop()}")

    elif opt==3:
        Peek()

    elif opt==4:
        Display()

    else:
        print("Invalid Option")