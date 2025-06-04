# Login credentials
username = "admin"
password = "123"

#creating empty dictionary
staff={}
patient={}
medicine={}
tests={}
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
 
#admin
def admin():
    while True:
        print('\n1.Add a new staff')
        print('2.View all staffs')
        print('3.Search for a particular staff')
        print('4.Update details of an existing staff')
        print('5.Delete staff')
        print('6.Exit')
        ch=int(input('Enter your choice :'))
        if ch==1:
            sid=input('Enter the Staff Id :')
            if sid in staff:
                print('Staff already exists!')
                return
            name=input("Enter the name :")
            gender=input("Gender :")
            designation=input('Enter the designation :')
            dateOfJoin=input('date of join :')
            location=input('location :')
            salary=input('salary :')
            age=input('age :')
            phone=input('phone :')
            blood=input('Blood group :')
            staff[sid]={'name':name,'gender':gender,'designation':designation,'date of join':dateOfJoin,'location':location,'salary':salary,'age':age,'phone':phone,'blood':blood}
            print('Staff added successfully !')
        elif ch==2:
            if not staff:
                print('Staff list is empty')
            else:
                for sid,i in staff.items():
                    print(f"staff id :{sid},name :{i['name']}, gender :{i['gender']},designation :{i['designation']},date of join :{i['date of join']},location :{i['location']},salary :{i['salary']},age :{i['age']} phone :{i['phone']}, blood :{i['blood']}")
        elif ch==3:
            sid=input('Enter the staff id :')
            if sid in staff:
                print('name :',staff[sid]['name'])
                print('gender :',staff[sid]['gender'])
                print('designation :',staff[sid]['designation'])
                print('date of join :',staff[sid]['date of join'])
                print('location :',staff[sid]['location'])
                print('salary :',staff[sid]['salary'])
                print('age :',staff[sid]['age'])
                print('phone :',staff[sid]['phone'])
                print('blood group :',staff[sid]['blood'])
                
            else:
                print('Staff not found !')
        elif ch==4:
            sid=input("Enter the id number :")
            if sid in staff:
                print('Enter the new details.....(leave empty if no changes)')
                name=input(f'updated name [{staff[sid]['name']}]') or staff[sid]['name']
                gender=input(f'edited gender [{staff[sid]['gender']}]') or staff[sid]['gender']
                designation=input(f'updated position [{staff[sid]['designation']}]') or staff[sid]['designation']
                dateOfJoin=input(f'edited date of join[{staff[sid]['date of join']}]') or staff[sid]['date of join']
                location=input(f'updated location [{staff[sid]['location']}]') or staff[sid]['location']
                salary=input(f'updated salary [{staff[sid]['salary']}]') or staff[sid]['salary']
                age=input(f'updated age [{staff[sid]['age']}]') or staff[sid]['age']
                phone=input(f'update phone number [{staff[sid]['phone']}]') or staff[sid]['phone']
                blood=input(f'edited blood group [{staff[sid]['blood']}]') or staff[sid]['blood']
                staff[sid]={'name':name,'gender':gender,'designation':designation,'date of join':dateOfJoin,'location':location,'salary':salary,'age':age,'phone':phone,'blood':blood}
                print('Updated name is :',staff[sid])
            else:
                print('Staff not found')
        elif ch==5:
            sid=input('Enter the staff id :')
            if sid in staff:
                print(staff[sid],'is deleted')
                del staff[sid]

            else:
                print('Staff not found !')
        elif ch==6:
            print('Exiting the System')
            break
        else:
            print('Invalid choice')
            
#Receptionist
def receptionist():
    while True:
        print("\n1. Add Patient")
        print("2. View Patient")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        #add patient
        if choice == "1":
            id=input("Enter patient ID:")
            if id in patient:
                print("ID already exist")
                return
            name=input("Enter patient name:")
            age=input("Enter patient age:")
            address=input("Enter patient address:")
            disease=input("Enter patient disease:")
            bg=input("Enter patient blood group:")
            ht=input("Enter patient weight:")
            wt=input("Enter patient height:")
            pn=input("Enter patient phone number:")
            patient[id]={"Name":name,"Age":age,"Address":address,"Disease":disease,"Blood Group":bg,"Weight":wt,"Height":ht,"Phone Number":pn}
            print("Medicine added successfully!\n")
                
        #view medicine
        elif choice == "2":
            if not patient:
                print("ID already exist")
                return
            else:
                print("Patient available!")
                for id,info in patient.items():
                    print(f"Patient ID:{id},Patient Name:{info["Name"]},Patient Age:{info["Age"]},Patient Address:{info["Address"]},Patient Disease:{info["Disease"]},Patient Blood Group:{info["Blood Group"]},Patient Weight:{info["Weight"]},Patient Height:{info["Height"]},Paitient Phone Number:{info["Phone Number"]}")

        #search medicine
        elif choice == "3":
            id=input("Enter patient ID:")
            if id in patient:
                print("Patient Found!")
                print("Patient ID:",id)
                print("Patient Name:",patient[id]["Name"])
                print("Patient Age:",patient[id]["Age"])
                print("Patient Address:",patient[id]["Address"])
                print("Patient Disease:",patient[id]["Disease"])
                print("Patient Blood Group:",patient[id]["Blood Group"])
                print("Patient Weight:",patient[id]["Weight"])
                print("Patient Height:",patient[id]["Height"])
                print("Patient Phone Number:",patient[id]["Phone Number"])
            else:
                print("Patient not found!")
        
        elif choice == "4":
            id=input("Enter patient id to edit:")
            if id in patient:
                print("Enter new details... (leave empty to keep current value)")
                name=input(f"Enter new patient name:[{patient[id]['Name']}]") or patient[id]['Name']
                age=input(f"Enter new patient age:[{patient[id]['Age']}]") or patient[id]['Age']
                address=input(f"Enter new patient address:[{patient[id]['Address']}]") or patient[id]['Address']
                disease=input(f"Enter new patient disease:[{patient[id]['Disease']}]") or patient[id]['Disease']
                bg=input(f"Enter new patient blood group:[{patient[id]['Blood Group']}]") or patient[id]['Blood Group']
                ht=input(f"Enter new patient weight:[{patient[id]['Weight']}]") or patient[id]['Weight']
                wt=input(f"Enter new patient height:[{patient[id]['Height']}]") or patient[id]['Height']
                pn=input(f"Enter new patient phone number:[{patient[id]['Phone Number']}]") or patient[id]['Phone Number']
            else:
                print("Patient not found")
                
                
        #delete patient       
        elif choice == "5":
            id=input("Enter patient id to delete:")
            if id in patient:
                del patient[id]
                print("Patient deleted!")
            else:
                print("Patient not found!")
        #exiting Receptionist
        elif choice == "6":
            print("Exiting  Receptionist...")
            break
        else:
            print("Invalid choice. Please try again.\n")
                        
            
        
    
   
def pharmacist():
    while True:
        print("\n1. Add Medicine")
        print("2. View Medicine")
        print("3. Search Medicine")
        print("4. Update Medicine")
        print("5. Delete Medicine")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        #add Medicine
        if choice == "1":
            id=input("Enter Medicine ID:")
            if id in medicine:
                print("ID already exist")
                return
            name=input("Enter medicine name:")
            gn=input("Enter medicine generic name:")
            cn=input("Enter medicine company name:")
            price=input("Enter medicine price:")
            medicine[id]={"Name":name,"generic":gn,"company":cn,"Price":price}
            print("Medicine added successfully!\n")
            
        #view Medicine
        elif choice == "2":
            if not medicine:
                print("Medicine not avilable!\n")
            else:
                print("Medicine available!")
                for id,info in medicine.items():
                    print(f"Medicine ID:{id},Medicine Name:{info["Name"]},Medicine Generic Name:{info["generic"]},Medicine Company Name:{info["company"]},Price:{info["Price"]}")
        
        #search Medicine
        elif choice == "3":
            id=input("Enter medicine ID:")
            if id in medicine:
                print("Medicine Found!")
                print("Medicine ID:",id)
                print("Medicine Name:",medicine[id]["Name"])
                print("Medicine Generic Name:",medicine[id]["generic"])
                print("Medicine Company Name:",medicine[id]["company"])
                print("Price:",medicine[id]["Price"])
            else:
                print("Medicine not found!")
        
        #update Medicine
        elif choice == "4":
            id=input("Enter medcine id to edit:")
            if id in medicine:
                print("Enter new details... (leave empty to keep current value)")
                name=input(f"Enter new medicine name:[{medicine[id]['Name']}]") or medicine[id]['Name']
                gn=input(f"Enter new medicine Generic Name:[{medicine[id]['generic']}]") or medicine[id]['generic']
                cn=input(f"Enter new medicine Company Name:[{medicine[id]['company']}]") or medicine[id]['company']
                price=input(f"Enter new medicine Price:[{medicine[id]['Price']}]") or medicine[id]['Price']
                medicine[id]={"Test ID:":id,"Name:":name,"generic:":gn,"company:":cn,"Price:":price}
                print("Medicine updated!")
            else:
                print("Medicine not found!")  
                
        #delete Medicine
        elif choice == "5":
            id=input("Enter medcine id to delete:")
            if id in medicine:
                del medicine[id]
                print("Medicine deleted!")
            else:
                print("Medicine not found!")
        #exiting Pharmacist
        elif choice == "6":
            print("Exiting  Pharmacist...")
            break
        else:
            print("Invalid choice. Please try again.\n")
    

#Lab Technician     
def technician():
    while True:
        print("\n1. Add Test")
        print("2. View Test")
        print("3. Search Test")
        print("4. Update Test")
        print("5. Delete Test")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        #add test
        if choice == "1":
            try:
                id = input("Enter test ID: ").strip()
                if not id:
                    raise ValueError("Test ID cannot be empty.")
                if id in tests:
                    print(" Test ID already exists.")
                    continue

                name = input("Enter test name: ").strip()
                if not name:
                    raise ValueError("Test name cannot be empty.")

                minimum = input("Enter test minimum range: ").strip()
                maximum = input("Enter test maximum range: ").strip()
                price = input("Enter test price: ").strip()

                if not minimum.isdigit() or not maximum.isdigit() or not price.isdigit():
                    raise ValueError("Minimum, maximum, and price must be numeric.")

                tests[id] = {"Name": name,"Minimum Range": minimum,"Maximum Range": maximum,"Price": price}
                print("Test added successfully!\n")
            except ValueError as e:
                print(f" Error: {e}")
            
        #view test 
        elif choice == "2":
            if not tests:
                print("Test not avilable!\n")
            else:
                print("Test member available!")
                for id,info in tests.items():
                    print(f"Test ID:,{id},Test Name:,{info["Name"]},Minimum Range:,{info["Minimum Range"]},Maximum Range:,{info["Maximum Range"]},Price:,{info["Price"]}")
        
        #search staff member
        elif choice == "3":
            id=input("Enter test ID:")
            if id in tests:
                print("Test Found!")
                print("Test ID:",id)
                print("Name:",tests[id]["Name"])
                print("Minimum Range:",tests[id]["Minimum Range"])
                print("Maximum Range:",tests[id]["Maximum Range"])
                print("Price:",tests[id]["Price"])
            else:
                print("Test not found!")
        
        #update staff member
        elif choice == "4":
            id=input("Enter test id to edit:")
            if id in tests:
                print("Enter new details... (leave empty to keep current value)")
                name=input(f"Enter new test name:[{tests[id]['Name']}]") or tests[id]['Name']
                minimum=input(f"Enter new test Minimum Range:[{tests[id]['Minimum Range']}]") or tests[id]['Minimum Range']
                maximum=input(f"Enter new test Maximum Range:[{tests[id]['Maximum Range']}]") or tests[id]['Maximum Range']
                price=input(f"Enter new test Price:[{tests[id]['Price']}]") or tests[id]['Price']
                tests[id]={"Test ID:":id,"Name:":name,"Minimum Range:":minimum,"Maximum Range:":maximum,"Price:":price}
                print("Test updated!")
            else:
                print("Test not found!")  
                
        #delete staff member
        elif choice == "5":
            id=input("Enter test id to delete:")
            if id in tests:
                del tests[id]
                print("Test deleted!")
            else:
                print("Test not found!")
        #exiting Technician
        elif choice == "6":
            print("Exiting  Technician...")
            break
        else:
            print("Invalid choice. Please try again.\n")


def menu():
     while True:
        print("\n1. Admin")
        print("2. Receptionist")
        print("3. Pharmacist")
        print("4. Lab Technician")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            admin()
        elif choice == "2":
            receptionist()
        elif choice == "3":
            pharmacist()
        elif choice == "4":
            technician()
        elif choice == "5":
            print("Exiting Client Management System...")
            break
        else:
            print("Invalid choice. Please try again.\n")
            
# Run the system
if login():
    menu()
        