# Login credentials
username = "admin"
password = "123"

#creating empty book dictionary
book={}

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

# Adding book
def add():
    bi=input("Enter book id:")
    if bi in book:
        print("Book already exist")
        return
    bt=input("Enter book title:")
    ba=input("Enter book author:")
    by=input("Enter book year:")
    bc=input("Enter book copies:")
    book[bi]={"title":bt,"author":ba,"year":by,"copy":bc}
    print("Book added successfully!\n")

#view all book
def view():
    if not book:
        print("Book not available!\n")
    else:
        print("Avilable book!")
        for bi,info in book.items():
            print(f"Book ID:{bi},Title:{info["title"]},Author:{info["author"]},Year:{info["year"]},Copies:{info["copy"]}")

#update
def update():
    bi=input("Enter book id to edit:")
    if bi in book:
        print("Enter new details... (leave empty to keep current value)")
        bt=input(f"Enter new book title:[{book[bi]['title']}]") or book[bi]['title']
        ba=input(f"Enter new book author:[{book[bi]['author']}]") or book[bi]['author']
        by=input(f"Enter new book year:[{book[bi]['year']}]") or book[bi]['year']
        bc=input(f"Enter new book copy:[{book[bi]['copy']}]") or book[bi]['copy']
        book[bi]={"title":bt,"author":ba,"year":by,"copy":bc}
        print("Book updated!")
    else:
        print("Book not found!")

#delete
def delete():
    bi=input("Enter book id to delete:")
    if bi in book:
        del book[bi]
        print("Books deleted!")
    else:
        print("Book not found!")
        
#search
def search():
    bi=input("Enter book id to delete:")
    if bi in book:
        print("Book found!")
        print("Book ID:",bi)
        print("Title:",book[bi]['title'])
        print("Author:",book[bi]['author'])
        print("Year:",book[bi]['year'])
        print("Copy:",book[bi]['copy'])
    else:
        print("Book not found")

#menu
def menu():
    while True:
        print("\n1. Add Book")
        print("2. View Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            search()
        elif choice == "6":
            print("Exiting Book Management System...")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the system
if login():
    menu()
        
        