import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="password")

mycursor = mydb.cursor()
mycursor.execute("create database if not exists food3")
mycursor.execute("use food3")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    Emp_id INT AUTO_INCREMENT PRIMARY KEY,
    ename VARCHAR(255) NOT NULL,
    emp_gender VARCHAR(10),
    eage INT,
    emp_phone BIGINT,
    pwd VARCHAR(255))""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    c_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cphone BIGINT,
    payment INT,
    pstatus VARCHAR(20),
    email VARCHAR(255),
    orderid INT,
    date DATE)""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Food (
    Food_id INT AUTO_INCREMENT PRIMARY KEY,
    Foodname VARCHAR(255) NOT NULL,
    Food_size VARCHAR(20),
    prize INT)""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS OrderFood (
    Orderf_id INT AUTO_INCREMENT PRIMARY KEY,
    C_id INT,
    Emp_id INT,
    Food_id INT,
    Food_qty INT,
    Total_price INT)""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS fee (
    roll INT AUTO_INCREMENT PRIMARY KEY,
    feedeposit INT,
    month VARCHAR(10))""")

def Customer():
    L = []
    c_id = int(input("Enter customer ID : "))
    L.append(c_id)
    name = input("Enter Customer Name: ")
    L.append(name)
    cphone = int(input("Enter customer phone number: "))
    L.append(cphone)
    payment = int(input("Enter payment method (1 for credit card, 2 for Debit Card): "))
    L.append(payment)
    pstatus = input("Enter the payment status: ")
    L.append(pstatus)
    email = input("Enter email id of the customer : ")
    L.append(email)
    orderid = input("Enter orderid: ")
    L.append(orderid)
    date = input("Enter the Date: ")
    L.append(date)
    custom = (L,)
    sql = "INSERT INTO customer (c_id, name, cphone, payment, pstatus, email, orderid, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, custom)
    mydb.commit()
    print(mycursor.rowcount,"customer details have been added ")

def Employee():
    L = []
    Emp_id = int(input("Enter Employee id: "))
    L.append(Emp_id)
    ename = input("Enter Employee Name: ")
    L.append(ename)
    emp_gender = input("Enter Employee Gender: ")
    L.append(emp_gender)
    eage = int(input("Enter Employee age: "))
    L.append(eage)
    emp_phone = int(input("Enter employee phone number: "))
    L.append(emp_phone)
    emp = tuple(L)  # Convert the list to a tuple
    sql = "INSERT INTO Employee (Emp_id, ename, emp_gender, eage, emp_phone) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, emp)
    mydb.commit()
    print(mycursor.rowcount," Employee details have been added. ")

def Food():
    L = []
    Food_id = int(input("Enter the Food id: "))
    L.append(Food_id)
    Foodname = input("Enter the Food Name: ")
    L.append(Foodname)
    Food_size = input("Enter Food size: ")
    L.append(Food_size)
    prize = int(input("Enter Prize of Food: "))
    L.append(prize)
    Food = (L,)
    sql = "INSERT INTO Food (Food_id, Foodname, Food_size, prize) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, Food)
    mydb.commit()

def OrderFood():
    L = []
    Order_id = int(input("Enter the Food Order id: "))
    L.append(Order_id)
    C_id = int(input("Enter the Customer id: "))
    L.append(C_id)
    Emp_id = int(input("Enter Employee id: "))
    L.append(Emp_id)
    Food_id = int(input("Enter Food id: "))
    L.append(Food_id)
    Food_qty = int(input("Enter Qty: "))
    L.append(Food_qty)
    Total_price = int(input("Enter Total_price: "))
    L.append(Total_price)
    OrderFood = tuple(L)  # Convert the list to a tuple
    sql = "INSERT INTO OrderFood (Orderf_id, C_id, Emp_id, Food_id, Food_qty, Total_price) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, OrderFood)
    mydb.commit()

def View():
    print("Select the search criteria: ")
    print("1. Employee")
    print("2. Customer")
    print("3. Food")
    print("4. Order Food")
    ch = int(input("Enter the choice 1 to 4: "))
    if ch == 1:
        Emp_id = int(input("Enter Employee ID to be searched: "))
        sql = "SELECT * FROM Employee WHERE Emp_id = %s"
        mycursor.execute(sql, (Emp_id,))
        res = mycursor.fetchall()
        for x in res:
            print(x)
    elif ch == 2:
        c_name = input("Enter Customer Name to be searched: ")
        sql = "SELECT * FROM Customer WHERE name = %s"
        mycursor.execute(sql, (c_name,))
        res = mycursor.fetchall()
        for x in res:
            print(x)
    elif ch == 3:
        sql = "SELECT * FROM Food"
        mycursor.execute(sql)
        res = mycursor.fetchall()
        for x in res:
            print(x)
    elif ch == 4:
        food_id = int(input("Enter Food ID to be searched : "))
        sql = "SELECT * FROM OrderFood WHERE Food_id = %s"
        mycursor.execute(sql, (food_id,))
        res = mycursor.fetchall()
        for x in res:
            print(x)

def MenuSet():
    while True:
        print("\n")
        print("Enter 1 to Add Employee")
        print("Enter 2 to Add Customer details")
        print("Enter 3 to Add Food Details")
        print("Enter 4 for Food Order")
        print("Enter 5 to view Food booking")
        
        try:
            userInput = int(input("Please Select an above option: "))
        except ValueError:
            exit("\nHey! That's Not A Number")
        else:
            print("\n")
            ch='y'
            while ch=='y':
                if userInput == 1:
                    Employee()
                elif userInput == 2:
                    Customer()
                elif userInput == 3:
                    Food()
                elif userInput == 4:
                    OrderFood()
                elif userInput == 5:
                    View()
                else:
                    print("Enter correct choice. . .")
                ch=input("Do you want to run again ??(y/n)")
MenuSet()