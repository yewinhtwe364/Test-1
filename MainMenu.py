from Administrator import Administrator as admin
from BookingOfficer import BookingOfficeMenu as BOM
from Member import MemberMenu as MM
from Accountant import AccountantMainMenu as AM
from Maintenance import MaintenanceMainMenu as MMM
def Main_menu():
    
    while True:
        print(f"""
                  {"=" * 40}
                    Main Menu
                    
                  1. Adminstrator
                  2. Booking Officer
                  3. Member
                  4. Accountant
                  5. Maintenance
                  6. Exit
                  {"=" * 40}
                  """)
        choice = input("Enter choice: ")
        if choice == "1":
            admin.Administrator_menu()
        elif choice == "2":
            BOM.booking_officer_menu()
        elif choice == "3":
            MM.MemberMainMenu()
        elif choice == "4":
            AM.accountant_main_menu()
        elif choice == "5":
            MMM.maintenance_main_menu()   
        elif choice == "6":
            print("Thank You! ")
            return
        else:
            print("Wrong Choice!")
if __name__ == "__main__":
    Main_menu()