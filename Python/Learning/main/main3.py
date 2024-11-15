# class Rectangle:
#     def __init__(self, length, breadth, height):
#         self.length = length
#         self.breadth = breadth
#         self.height = height

#     def Area(self):
#         print(self.length * self.breadth)

#     def Volume(self):
#         print(self.length * self.breadth * self.height)

# l = float(input("Length: "))
# b = float(input("Breadth: "))
# h = float(input("Height: "))

# rectangle = Rectangle(l,b,h)
# rectangle.Area()
# rectangle.Volume()

# class MyClass:
#     x=5

# p = MyClass()
# print(p.x)

# class Dog:
#     atr1 = "Mammal"

# obj = Dog()

# print(obj.atr1)
# print(Dog.atr1)

# class Student:
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello {self.name}! I am {self.age} years old")

# obj1 = Student("101", "ABC", 18)
# obj2 = Student("102", "DEF", 19)
# obj3 = Student("103", "GHI", 20)
# obj4 = Student("104", "JKL", 21)

# print(obj1.name)
# print(obj3.age)
# print(obj4.id)

# obj3.greet()


# class Addition:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.result = self.x + self.y

# x = float(input("Enter X: "))
# y = float(input("Enter Y: "))

# add =Addition(x,y)
# print(add.result)


# class Vehicle:
#     def __init__(self, color, fuel):
#         self.color = color
#         self.fuel = fuel
        
# class Car(Vehicle):
#     def __init__(self, color, fuel, num_wheels):
#         self.num_wheels = num_wheels
#         super().__init__(color, fuel)

#     def display(self):
#         print(f"Car Color: {self.color}")
#         print(f"Fuel Type: {self.fuel}")
#         print(f"No. of Wheels: {self.num_wheels}")

# class Bicycle(Vehicle):
#     def __init__(self, color, fuel, type):
#         self.type = type
#         super().__init__(color, fuel)

#     def display(self):
#         print(f"Bicycle Color: {self.color}")
#         print(f"Fuel Type: {self.fuel}")
#         print(f"Type: {self.type}")

# car = Car("Blue","Petrol",4)
# bicycle = Bicycle("Red","Electric","BMS")

# car.display()
# bicycle.display()


# class Login:
#     def __init__(self, name, email, password):
#         self.name = name
#         self._email = email
#         self.__password = password

# login = Login("Muaz", "muaz@gmail.com","muaz12345")
# print(login.name)
# print(login._email)
# print(login._Login__password)


# class Dad:
#     def func1(self):
#         print("Func1")

# class Mom:
#     def func2(self):
#         print("Func2")
    
# class Child(Dad, Mom):
#     def func3(self):
#         print("Func2")




s = 7
for i in range(1,5):
    print(" "*s, end='')
    for j in range(i):
        print(i,end=" ")
    print()
    s-=2

































































