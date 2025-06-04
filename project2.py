#login credentials
username = "admin"
password = "123"

#creating empty dictionary
book={}
member={}

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
    
#add book    
def add():
    import random
    id=str(random.randint(10000, 99999))
    if id in book:
        print("Book id already exists!")
    print("Your book id is: ", id)
    n=input("Enter book name:") #n=name
    a=input("Enter book author:")#a=author
    c=input("Enter book category:")#c=category
    p=input("Enter book price:")#p=price
    c=input("Enter book copies:")#c=copies
    book[id]={"Name":n,"Author":a,"Category":c,"Price":p,"Copies":c}
    print("Book added successfully!\n")
    
#update   
def update():
    id=input("Enter book id to edit:")
    if id in book:
        print("Enter new details... (leave empty to keep current value)")
        p=input(f"Enter new book price:[{book[id]["Price"]}]") or book[id]["Price"]
        c=input(f"Enter new book copies:[{book[id]["Copies"]}]") or book[id]["Copies"]
        book[id]={"Price":p,"Copies":c}
        print("Book updated!")
    else:
        print("Book id not found!")

#delete
def delete():
    id=input("Enter book id to delete:")
    if id in book:
        del book[id]
        print("Book deleted!")
    else:
        print("Book id not found!")
        
#view        
def view():
    if not book:
        print("Book not available!\n")
    else:
        print("Avilable book!")
        for id,info in book.items():
            print(f"Book id: {id},Book name: {info["Name"]},Book author: {info["Author"]},Book category: {info["Category"]},Book price: {info["Price"]},Book copies: {info["Copies"]}")

#search
def search():
    id=input("Enter book id to search:")
    if id in book:
        print(f"Book id: {id},Book name: {book[id]["Name"]},Book author: {book[id]["Author"]},Book category: {book[id]["Category"]},Book price: {book[id]["Price"]},Book copies: {book[id]["Copies"]}")
    else:
        print("Book id not found")

#add member
def new_member():
    import random
    id=str(random.randint(1000, 9999))
    if id in member:
        print("Member id already exists!")
    print("Your member id is: ", id)
    n=input("Enter member name:") #n=name
    m=input("Enter member mobile number:")
    e=input("Enter member email id:")
    member[id]={"Name":n,"Mobile":m,"Email":e}
    print("Member added!")
  
#view member    
def view_member():
    if not member:
        print("Member not available!")
    else:
        print("Available member!")
        for id,info in member.items():
            print(f"Member id: {id},Member name: {info["Name"]},Member mobile number: {info["Mobile"]},Member email id: {info["Email"]}")
            
#borrow book
#enter member id and book id borrow the book.if copies avilable reduce copies by 1 and add book id to member borrowed list.otherwise print book bot avilable.
def borrow():
    id=input("Enter member id to borrow book:")
    if id in member:
        book_id=input("Enter book id to borrow:")
        if book_id in book:
            if book[book_id]["Copies"] > "0":
                book[book_id]["Copies"] -= "1"
                if "Borrowed" not in member[id]:
                    member[id]["Borrowed"] = []
                    member[id]["Borrowed"].append(book_id)
                else:
                    member[id]["Borrowed"].append(book_id)
                    print("Book borrowed!")
            else:
                print("Book not available!")
        else:
            print("Book id not found")
    else:
        print("Member id not found")
        
                    
    
    
    
    
    
    
    
    
    
def menu():
    while True:
        print("\n1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View Book")
        print("5. Search Book")
        print("6. New Member")
        print("7. View Member")
        print("8. Borrow Book")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            update()
        elif choice == "3":
            delete()
        elif choice == "4":
            view()
        elif choice == "5":
            search()
        elif choice == "6":
            new_member()
        elif choice == "7":
            view_member()
        elif choice == "8":
            borrow()
        elif choice == "9":
            print("Exiting Book Management System...")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the system
if login():
    menu()