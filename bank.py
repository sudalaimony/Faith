# Credentials
admin_username = "admin"
admin_password = "123"

# Demo customer credentials
customer_username = "customer"
customer_password = "123"
#creating empty dictionaries
admin={}

# ------------------ Login ------------------

def login():
    print("--- Welcome to Bank Management System ---")
    uname = input("Username: ")
    pwd = input("Password: ")
    if uname == admin_username and pwd == admin_password:
        print("Admin login successful!\n")
        return "admin"
    elif uname == customer_username and pwd == customer_password:
        print("Customer login successful!\n")
        return "customer"
    else:
        print("Invalid credentials!\n")
        return None

# ------------------ Admin Menu ------------------

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. View All Customers")
        print("5. Search Customer")
        print("6. Back to Role Selection")
        
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
            break
        else:
            print("Invalid choice. Try again.")
        
    
#account number
def add():
    import random
    id = str(random.randint(1000000000, 9999999999))
    while id in admin:
        id = str(random.randint(1000000000, 9999999999))
    print("Your account number is:", id)

    n = input("Enter account name: ")
    while len(n) > 30:
        print("Name should not be more than 30 characters")
        n = input("Enter account name: ")

    type = ""
    while type.lower() not in ["saving", "current"]:
        type = input("Enter account type (saving/current): ")
        if type.lower() not in ["saving", "current"]:
            print("Invalid choice. Please choose saving or current")

    try:
        b = int(input("Enter account balance: "))
        mb = int(input("Enter account minimum balance: "))
    except ValueError:
        print("Balance must be an integer. Aborting account creation.")
        return

    while True:
        try:
            m = int(input("Enter customer mobile number (10 digits): "))
            if len(str(m)) == 10:
                break
            else:
                print("Mobile number should be exactly 10 digits.")
        except ValueError:
            print("Invalid input. Enter digits only.")

    while True:
        e = input("Enter customer email id: ")
        if e.endswith("@gmail.com") and len(e) > 10:
            break
        else:
            print("Invalid email! Please enter a valid email address.")
    # while True:
    #     e = input("Enter customer email id (must be @gmail.com): ")
    #     if e.endswith("@gmail.com") and len(e) > 10:
    #         local_part = e[:-10]  # everything before '@gmail.com'
    #         if local_part.replace('.', '').replace('-', '').replace('_', '').isalnum():
    #             break
    #         else:
    #             print("Invalid characters in email local part.")
    #     else:
    #         print("Invalid email! Please enter a valid @gmail.com email address.")


    a = random.randint(1000, 9999)
    print(f"Generated 4-digit account PIN: {a}")

    admin[id] = {
        "name": n,
        "type": type,
        "balance": b,
        "min_balance": mb,
        "mobile": m,
        "email": e,
        "pin": a
    }
    print("Account created successfully!")
    
#update 
def update():
    id = input("Enter account number: ")
    if id in admin:
        print("Account exists")
        print("Enter new details... (leave empty to keep current value)")
        while True:
            m = input(f"Enter new customer mobile number [{admin[id]['mobile']}]: ") or str(admin[id]["mobile"])
            if m.isdigit() and len(m) == 10:
                break
            else:
                print("Invalid mobile number! It must be exactly 10 digits and numeric.")
        e = input(f"Enter new customer email id [{admin[id]['email']}]: ") or admin[id]["email"]
        admin[id]["mobile"] = int(m)
        admin[id]["email"] = e
        print("Account updated successfully!")
    else:
        print("Account does not exist!")


#delete
def delete():
    id = input("Enter account number: ")
    if id in admin:
        del admin[id]
        print("Account deleted successfully!")
    else:
        print("Account does not exist!")
    
#view  
def view():
    if not admin:
        print("No customers!")
    else:
        for id, details in admin.items():
            print("Accound details!")
            print(f"Account Number: {id}")
            print(f"Customer Name: {details["name"]}")
            print(f"Account Type: {details["type"]}")
            print(f"Account Balance: {details["balance"]}")
            print(f"Minimum Balance: {details["min_balance"]}")
            print(f"Customer Mobile Number: {details["mobile"]}")
            print(f"Customer Email ID: {details["email"]}")
            print(f"Customer PIN: {details["pin"]}")
            print("\n")
        
#search customer 
def search():
    id = input("Enter account number: ")
    if id in admin:
        print("Account exists")
        print("Account details!")
        print(f"Account Number: {id}")
        print(f"Customer Name: {admin[id]["name"]}")
        print(f"Account Type: {admin[id]["type"]}")
        print(f"Account Balance: {admin[id]["balance"]}")
        print(f"Minimum Balance: {admin[id]["min_balance"]}")
        print(f"Customer Mobile Number: {admin[id]["mobile"]}")
        print(f"Customer Email ID: {admin[id]["email"]}")
        print(f"Customer PIN: {admin[id]["pin"]}")
    else:
        print("Account does not exist!")

# ------------------ Customer Menu ------------------

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            balance()
        elif choice == "4":
            transfer()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

# deposit
def deposit():
    id = input("Enter account number: ")
    if id in admin:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            if amount > 49999:
                pan = input("Enter your PAN Card number: ")
                if pan in admin:
                    admin[id]["balance"] += amount
                else:
                    pan = input("Enter PAN Card number to add: ")
                    admin[id]["pan"]=pan
                    admin[id]["balance"] += amount
                print("Deposit successful!")
            else:
                admin[id]["balance"] += amount
                print("Deposit successful!")
        else:
            print("Invalid amount. Please enter a positive number.")
    else:
        print("Account does not exist!")
        
#withdraw
def withdraw():
    id = input("Enter account number: ")
    if id in admin:
        amount = int(input("Enter amount to withdraw: "))
        if amount > 0:
            if amount > 49999:
                pan = input("Enter your PAN Card number: ")
                admin[id]["pan"]=pan
                if amount <=admin[id]["balance"]-admin[id]["min_balance"]:
                            admin[id]["balance"] -= amount
                            print("Withdrawal successful!")
                else:
                        print("Insufficient balance!")     
            else:
                if amount <=admin[id]["balance"]-admin[id]["min_balance"]:
                        admin[id]["balance"] -= amount
                        print("Withdrawal successful!")
                else:
                    print("Insufficient balance!")
        else:
            print("Invalid amount. Please enter a positive number.")
    else:
        print("Account does not exist!")
        
#balance
def balance():
    id = input("Enter account number: ")
    if id in admin:
        print("Your current balance is: ", admin[id]["balance"])
    else:
        print("Account does not exist!")

#transfer 
def transfer():
    id = input("Enter your account number: ")
    to_id = input("Enter recipient's account number: ")
    if id in admin and to_id in admin:
        amount = int(input("Enter amount to transfer: "))
        if amount <=0:
            print("Invalid amount. Please enter a positive number.")
        elif amount >49999:
            pan = input("Enter PAN Card number: ")
            admin[id]["pan"]=pan
            if amount <= admin[id]["balance"]-admin[id]["min_balance"]:
                        admin[id]["balance"] -= amount
                        admin[to_id]["balance"] += amount
                        print("Transferred Amount Successfully!")
            else:
                print("Insufficient balance!")
                
        else:
            if amount <= admin[id]["balance"]-admin[id]["min_balance"]:
                    admin[id]["balance"] -= amount
                    admin[to_id]["balance"] += amount
                    print("Transferred Amount Successfully!")
            else:
                print("Insufficient balance!")
    else:
        print("Account does not exist!")
                        
# ------------------ Main ------------------

def main():
    role = login()
    if role == "admin":
        while True:
            print("\n--- Admin Role Menu ---")
            print("1. Admin Menu")
            print("2. Customer Menu")
            print("3. Logout")

            choice = input("Select an option: ")
            if choice == "1":
                admin_menu()
            elif choice == "2":
                customer_menu()
            elif choice == "3":
                print("Logged out.\n")
                break
            else:
                print("Invalid choice.")
    elif role == "customer":
        customer_menu()
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()