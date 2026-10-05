from Member import ViewAvailableClass as VAC
from Member import RequestBooking as RB
from Member import ViewBookingHistory as VBH

def MemberMainMenu():
    memberID = input("\nEnter your MemberID: ")
    while True:
        
        found = False
        try:
            with open("txt/Member.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[0] == memberID.strip():
                        found = True
                        break
            if found:
                print(f"""
                    {"=" * 40}
                    Member Main Menu
                            
                    1. View Available Class
                    2. Request Booking
                    3. View Booking History
                    4. Back to Main menu
                    {"=" * 40}
                    """)

                choice = input("Enter choice: ")

                if choice == "1":
                    VAC.view_available_classes()
                elif choice == "2":
                    RB.request_booking(memberID)
                elif choice == "3":
                    VBH.view_booking_history(memberID)
                elif choice == "4":
                    return
                else:
                    print("Wrong Choice!")
            else:
                print("Invalid Member ID, Go to Booking Officer to register!")
                return
        except FileNotFoundError:
            print("File is not found!")