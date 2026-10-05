from Administrator import AddNewClass as AC
from Administrator import UpdateClassSchedule as U
from Administrator import RemoveClass as R
from Administrator import ViewClass as VC
from Administrator import ViewMember as VM
from Administrator import ViewBooking as VB
from Administrator import ViewPayment as VP
from Administrator import GenerateAllReport as GR
def Administrator_menu():
    
    while True:
        print(f"""
            {"=" * 40}
            STUDIO ADMINISTRATOR MENU
        
            1. Add New Class
            2. Update Class Schedule
            3. Remove Class
            4. View Class
            5. View Members
            6. View Bookings
            7. View Payments
            8. Generate Overall Report
            9. Back to Main Menu
            {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            AC.Add_New_Class()
        elif choice == "2":
            U.Update_Class_Schedule()
        elif choice == "3":
            R.Remove_Class()
        elif choice == "4":
            VC.View_Class()
        elif choice == "5":
            VM.View_Member()
        elif choice == "6":
            VB.View_Booking()
        elif choice == "7":
            VP.View_Payment()
        elif choice == "8":
           GR.Generate_All_Report()
        elif choice == "9":
            return
        else:
            print("Wrong Choice, Try again")
        

        
