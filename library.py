# Login credentials
username = "admin"
password = "123"

# Creating empty dictionaries
book = {}
member = {}

# Login function
def login():
    print("Client Management System")
    uname = input("Username: ")
    pwd = input("Password: ")
    if uname == username and pwd == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials!\n")
        return False

# Book management function
def book_menu():
    while True:
        print("\n=== Book Management Menu ===")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View Books")
        print("5. Search Book")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            view_books()
        elif choice == "5":
            search_book()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

# Add book
def add_book():
    import random
    id = str(random.randint(10000, 99999))
    while id in book:
        id = str(random.randint(10000, 99999))
    print("Your book id is:", id)
    n = input("Enter book name: ")
    a = input("Enter book author: ")
    c = input("Enter book category: ")
    p = input("Enter book price: ")
    copies = input("Enter book copies: ")
    book[id] = {"Name": n, "Author": a, "Category": c, "Price": p, "Copies": copies}
    print("Book added successfully!\n")

# Update book
def update_book():
    id = input("Enter book id to edit: ")
    if id in book:
        print("Enter new details... (leave empty to keep current value)")
        p = input(f"Enter new book price [{book[id]['Price']}]: ") or book[id]["Price"]
        c = input(f"Enter new book copies [{book[id]['Copies']}]: ") or book[id]["Copies"]
        book[id]["Price"] = p
        book[id]["Copies"] = c
        print("Book updated!")
    else:
        print("Book id not found!")

# Delete book
def delete_book():
    id = input("Enter book id to delete: ")
    if id in book:
        del book[id]
        print("Book deleted!")
    else:
        print("Book id not found!")

# View books
def view_books():
    if not book:
        print("No books available!\n")
    else:
        print("Available Books:")
        for id, info in book.items():
            print(f"ID: {id}, Name: {info['Name']}, Author: {info['Author']}, Category: {info['Category']}, Price: {info['Price']}, Copies: {info['Copies']}")

# Search book
def search_book():
    id = input("Enter book id to search: ")
    if id in book:
        info = book[id]
        print(f"ID: {id}, Name: {info['Name']}, Author: {info['Author']}, Category: {info['Category']}, Price: {info['Price']}, Copies: {info['Copies']}")
    else:
        print("Book id not found")

# Member management
def member_menu():
    while True:
        print("\n=== Member Management Menu ===")
        print("1. Add Member")
        print("2. View Members")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

# Add member
def add_member():
    import random
    id = str(random.randint(1000, 9999))
    while id in member:
        id = str(random.randint(1000, 9999))
    print("Your member id is:", id)
    n = input("Enter member name: ")
    m = input("Enter member mobile number: ")
    e = input("Enter member email id: ")
    l1=[]
    member[id] = {"Name": n,"Mobile": m,"Email": e,"Borrowed":l1}
    print("Member added!")

# View members
def view_members():
    if not member:
        print("No members available!")
    else:
        print("Available Members:")
        for id, info in member.items():
            borrowed = info.get("Borrowed", [])
            print(f"ID: {id}, Name: {info['Name']}, Mobile: {info['Mobile']}, Email: {info['Email']}, Borrowed Books: {borrowed}")

# Borrow, return, and view borrowed books
def borrow():
    while True:
        print("\n=== Borrow Menu ===")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. View Borrowed Books")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter member id to borrow book: ")
            if id in member:
                book_id = input("Enter book id to borrow: ")
                if book_id in book:
                    if int(book[book_id]["Copies"]) > 0:
                        book[book_id]["Copies"] = str(int(book[book_id]["Copies"]) - 1)
                        member[id]["Borrowed"].append(book_id)
                        print("Book borrowed successfully!")
                    else:
                        print("Book not available!")
                else:
                    print("Book id not found")
            else:
                print("Member id not found")

        elif choice == "2":
            id = input("Enter member id to return book: ")
            if id in member and member[id]["Borrowed"]:
                print("Borrowed books:", member[id]["Borrowed"])
                book_id = input("Enter book id to return: ")
                if book_id in member[id]["Borrowed"]:
                    member[id]["Borrowed"].remove(book_id)
                    if book_id in book:
                        book[book_id]["Copies"] = str(int(book[book_id]["Copies"]) + 1)
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed by the member.")
            else:
                print("Member id not found or no books borrowed.")

        elif choice == "3":
            id = input("Enter member id : ")
            if id in member and member[id]["Borrowed"]:
                print(f"\nBorrowed Books by Member {id} ({member[id]['Name']}):")
                for b_id in member[id]["Borrowed"]:
                    if b_id in book:
                        info = book[b_id]
                        print(f"Book ID: {b_id}, Name: {info['Name']}")
            else:
                print("No borrowed books for this member.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

# Main menu
def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("1. Book Management")
        print("2. Member Management")
        print("3. Borrow System")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_menu()
        elif choice == "2":
            member_menu()
        elif choice == "3":
            borrow()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the system
if login():
    main_menu()
