def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y==0:
        print("Can't Divide by Zero")
    else:
        return x/y

print("Choose Which Operation You Want To Do")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

opt=int(input("Enter Which Operation: "))
x=int(input("X: "))
y=int(input("Y: "))

if opt==1:
    print(f"X + Y = {addition(x,y)}")
elif opt==2:
    print(f"X - Y = {subtraction(x,y)}")
elif opt==3:
    print(f"X * Y = {multiplication(x,y)}")
elif opt==4:
    print(f"X / Y = {division(x,y)}")
else:
    print("Invalid Option")

    