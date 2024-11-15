stack=[]
top=None
def Push(item):
    global top
    if len(stack)==maxi:
        print("Stack Overflow")
    else:
        stack.append(item)
        top=len(stack)-1

def Pop():
    global top
    if stack==[]:
        print("Stack Underflow")
    else:
        x=stack.pop()
        if len(stack)==0:
            top=None
        else:
            top-=1
        return x

def Peek():
    if stack==[]:
        print("Stack is Empty")
    else:
        print(f"Top: {stack[top]}")

def Display():
    if stack==[]:
        print("Stack is Empty")
    else:
        print(f"Top: {stack[top]}")
        for i in range(top-1,-1,-1):
            print(stack[i])

while True:
    print("Stack Operations")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")

    opt=int(input("Enter your choice: "))
    maxi=int(input("Enter max size of the stack: "))

    if opt==1:
        bookno=int(input("Book No.: "))
        bookname=input("Book Name: ")
        itemL=[bookno,bookname]
        Push(itemL)

    elif opt==2:
        print(f"Successfully Deleted: {Pop()}")

    elif opt==3:
        Peek()

    elif opt==4:
        Display()

    else:
        print("Invalid Option")