# string = input("Enter a word: ")

# for i in string:
#     if i in 'AEIOUaeiou':
#         print("Vowel Detected")
#         break

student_data = {}

def display():
    for key,value in student_data.items():
        print(key, value)

def add_record():
    i = 1

    while True:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")

        data = {"Name":name, "Age":age, "Gender":gender}
        student_data[f'student{i}'] = data
        i += 1

        opt = input("Do you want to add more data? (yes or no): ").lower()
        if opt=="no":
            break

def remove_record():
    while True:
        display()

        remove_choice = input("What record do you want to remove: ").lower()
        student_data.pop(remove_choice)

        opt = input("Do you want to remove more data? (yes or no): ").lower()
        if opt=="no":
            break

    display()

add_record()
remove_record()