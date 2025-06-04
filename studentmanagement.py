# Student Management System
# Login credentials
username = "admin"
password = "123456"

# Create empty dictionary for students
students = {}

# Login function
def login():
    print("Student Management System")
    uname = input("Username: ")
    pwd = input("Password: ")
    if uname == username and pwd == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials!\n")
        return False

# Function to add student
def add():
    roll = input("Enter roll number: ")
    if roll in students:
        print("Student already exists.")
        return
    name = input("Enter name: ")
    clas = input("Enter class: ")
    phone = input("Enter phone number: ")
    students[roll] = {"name": name, "class": clas, "phone": phone}
    print("Student added successfully!\n")

# Function to edit student
def edit():
    roll = input("Enter roll number to edit: ")
    if roll in students:
        print("Enter new details... (leave empty to keep current value)")
        name = input(f"New name [{students[roll]['name']}]: ") or students[roll]['name']
        clas = input(f"New class [{students[roll]['class']}]: ") or students[roll]['class']
        phone = input(f"New phone [{students[roll]['phone']}]: ") or students[roll]['phone']
        students[roll] = {"name": name, "class": clas, "phone": phone}
        print("Student updated!\n")
    else:
        print("Student roll number not found.\n")

# Function to delete student
def delete():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted!\n")
    else:
        print("Student not found.\n")

# Function to search student
def search():
    roll = input("Enter roll number to search: ")
    if roll in students:
        print("Student found")
        print("Roll:", roll)
        print("Name:", students[roll]['name'])
        print("Class:", students[roll]['class'])
        print("Phone:", students[roll]['phone'], "\n")
    else:
        print("Student not found.\n")

# Function to list students
def list_students():
    if not students:
        print("No students found.\n")
    else:
        print("Student List:")
        for roll, info in students.items():
            print(f"Roll: {roll}, Name: {info['name']}, Class: {info['class']}, Phone: {info['phone']}")

# Menu function
def menu():
    while True:
        print("\n1. Add Student")
        print("2. Edit Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            edit()
        elif choice == "3":
            delete()
        elif choice == "4":
            search()
        elif choice == "5":
            list_students()
        elif choice == "6":
            print("Exiting Student Management System...")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the system
if login():
    menu()