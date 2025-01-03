print("Welcome to Razan's Calculator")
print("------------------------------")
x=float(input("Enter the First Number: "))
Operator=input("Choose From the Following Operators: +,-,x,%: ")
y=float(input("Enter the Second Number: "))
if Operator=='+':
      print("Result of",x,"+",y, "is = ",x+y)
elif Operator=='-':
    print("Result of",x,"-",y, "is = ",x-y)
elif Operator=='x':
    print("Result of",x,"x",y, "is = ",x*y)
elif Operator=='%':
    if y==0:
        print("Division by 0 is Not Possible.")
    else:
        print("Result of",x,"%",y, "is = ",x/y)
else:
    print("Hehehe You are using wronggg operattor")

