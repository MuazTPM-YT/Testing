students=["Muaz","Razan","Nafih"]
stack=[]

def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False

def Push(student):
    search=input("Search: ")
    if search in student:
        stack.append(search)
    else:
        print("Name not found")

Push(students,stack)
print(stack)

def Pop(student):
    if isEmpty(stack):
        print("Stack Underflow")
    else:
        i=student.pop()
    return i

print(Pop(stack))


