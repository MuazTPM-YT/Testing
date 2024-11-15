S=[]
top=None 

def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False

def push(stk, item):
    stk.append(item)
    top=len(stk)-1

def s_pop(stk):
    if isEmpty(stk):
        print("Stack Underflow")
    else:
        i=stk.pop()
        print("Stack Popped Successfully")
        if len(stk)==0:
            top=None
    return i

def display(stk):
    if isEmpty(stk):
        print("Stack is Empty")
    else:
        top=len(stk)-1
        print(f"{stk[top]} <--- Top")
        for x in range(top-1,-1,-1):
            print(stk[x])

while True:
    print("Choose the options given below")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    opt=int(input(">>> "))

    if opt==1:
        item=input("What do you want to add to the stack?: ")
        push(S,item)
    
    elif opt==2:
        s_pop(S)

    elif opt==3:
        display(S)
    
    elif opt==4:
        print("Thank you for using my program.")
        break

    else:
        print("Invalid Option")