import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', passwd='password', database='Students')

cur=db.cursor()
cur.execute("CREATE TABLE Student(RollNo INT PRIMARY KEY, Name VARCHAR(30), Marks DECIMAL(5,2));")

cur.execute("INSERT INTO Student VALUES(01, 'Muaz Ismail Mohammed', 99.99)")
cur.execute("INSERT INTO Student VALUES(02, 'Muhammad Razan', 98.99)")
cur.execute("INSERT INTO Student VALUES(03, 'Ammaar Hussain', 97.99)")
cur.execute("INSERT INTO Student VALUES(04, 'Muhammad Ashil', 96.99)")
cur.execute("INSERT INTO Student VALUES(05, 'Nihad Abdul Rahman', 95.99)")

db.commit()

cur.execute("SELECT * FROM Student")

recordone=cur.fetchone()
print(recordone)

recordmany=cur.fetchmany(3)
print(recordmany)