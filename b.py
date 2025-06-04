import random

# Credentials
admin_username = "admin"
admin_password = "123"

# Demo customer credentials
customer_username = "customer"
customer_password = "123"

# Dictionary to store customer account data
accounts = {}

# ------------------ Login ------------------

def login():
    print("=== Welcome to Bank Management System ===")
    uname = input("Username: ")
    pwd = input("Password: ")
    if uname == admin_username and pwd == admin_password:
        print("✅ Admin login successful!\n")
        return "admin"
    elif uname == customer_username and pwd == customer_password:
        print("✅ Customer login successful!\n")
        return "customer"
    else:
        print("❌ Invalid credentials!\n")
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

        choice = input("Enter choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            update_customer()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            display_customers()
        elif choice == "5":
            search_customer()
        elif choice == "6":
            break
        else:
            print("❌ Invalid choice!")

def add_customer():
    id = str(random.randint(1000000000, 9999999999))
    while id in accounts:
        id = str(random.randint(1000000000, 9999999999))
    print(f"Generated Account No: {id}")
    
    name = input("Name: ")[:30]
    acc_type = input("Type (saving/current): ").lower()
    if acc_type not in ["saving", "current"]:
        print("❌ Invalid account type.")
        return

    try:
        balance = int(input("Balance: "))
        min_bal = int(input("Minimum Balance: "))
    except ValueError:
        print("❌ Balance must be integer.")
        return

    mobile = input("Mobile (10 digits): ")
    if not (mobile.isdigit() and len(mobile) == 10):
        print("❌ Invalid mobile.")
        return

    email = input("Email (must end with @gmail.com): ")
    if not email.endswith("@gmail.com"):
        print("❌ Invalid email.")
        return

    pin = random.randint(1000, 9999)
    print(f"Generated PIN: {pin}")

    accounts[id] = {
        "name": name,
        "type": acc_type,
        "balance": balance,
        "min_balance": min_bal,
        "mobile": mobile,
        "email": email,
        "pin": pin
    }
    print("✅ Customer Added.")

def update_customer():
    id = input("Account Number: ")
    if id not in accounts:
        print("❌ Not found.")
        return
    mobile = input("New Mobile (Leave blank to keep): ") or accounts[id]["mobile"]
    email = input("New Email (Leave blank to keep): ") or accounts[id]["email"]
    accounts[id]["mobile"] = mobile
    accounts[id]["email"] = email
    print("✅ Updated.")

def delete_customer():
    id = input("Account Number: ")
    if id in accounts:
        del accounts[id]
        print("✅ Deleted.")
    else:
        print("❌ Not found.")

def display_customers():
    if not accounts:
        print("⚠️ No customers.")
    for id, data in accounts.items():
        print(f"\nAccount: {id}")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")

def search_customer():
    id = input("Account Number: ")
    if id in accounts:
        for key, value in accounts[id].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("❌ Not found.")

# ------------------ Customer Menu ------------------

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            transfer()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice!")

def deposit():
    id = input("Account Number: ")
    if id in accounts:
        try:
            amount = int(input("Amount to deposit: "))
        except ValueError:
            print("❌ Must be number.")
            return
        accounts[id]["balance"] += amount
        print("✅ Deposit done. New balance:", accounts[id]["balance"])
    else:
        print("❌ Account not found.")

def withdraw():
    id = input("Account Number: ")
    if id in accounts:
        try:
            amount = int(input("Amount to withdraw: "))
        except ValueError:
            print("❌ Must be number.")
            return
        if accounts[id]["balance"] - amount >= accounts[id]["min_balance"]:
            accounts[id]["balance"] -= amount
            print("✅ Withdrawn. New balance:", accounts[id]["balance"])
        else:
            print("❌ Insufficient balance.")
    else:
        print("❌ Account not found.")

def check_balance():
    id = input("Account Number: ")
    if id in accounts:
        print("✅ Current balance:", accounts[id]["balance"])
    else:
        print("❌ Account not found.")

def transfer():
    from_id = input("Your Account No: ")
    to_id = input("Recipient Account No: ")
    if from_id in accounts and to_id in accounts:
        try:
            amount = int(input("Amount: "))
        except ValueError:
            print("❌ Must be number.")
            return
        if accounts[from_id]["balance"] - amount >= accounts[from_id]["min_balance"]:
            accounts[from_id]["balance"] -= amount
            accounts[to_id]["balance"] += amount
            print("✅ Transfer complete.")
        else:
            print("❌ Insufficient balance.")
    else:
        print("❌ One of the accounts not found.")

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
                print("✅ Logged out.\n")
                break
            else:
                print("❌ Invalid choice.")
    elif role == "customer":
        customer_menu()
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
