# Booking office menu
from BookingOfficer import MemberRegistration as MR
from BookingOfficer import UpdateMemberInformation as UM
from BookingOfficer import DeleteMember as DM
from BookingOfficer import BookingClass as BC
from BookingOfficer import BookingCancelling as BCC
from BookingOfficer import BookingReschedule as BR
from BookingOfficer import RecordAttendence as RA
from BookingOfficer import ViewMemberAttendanceHistory as VMAH
from BookingOfficer import DeleteBooking as DB
from BookingOfficer import ViewBookingRequest as VBR
def booking_officer_menu():

    while True:

        print(f"""
                {"=" * 40}
                BOOKING OFFICER MENU
                
                1.  Register Member
                2.  Update Member Information
                3.  Delete Member
                4.  Delete Booking 
                5.  Booking Class
                6.  Booking Cancellations
                7.  Booking Reschedule
                8.  Record Member Attendance
                9.  View Member Attendance History 
                10. View Booking Request
                11. Back to Main Menu
                {"=" * 40}
            """)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            MR.member_registration()

        elif choice == "2":
            UM.update_member()

        elif choice == "3":
            DM.delete_member()

        elif choice == "4":
            DB.delete_booking()

        elif choice == "5":
            BC.class_booking()

        elif choice == "6":
            BCC.booking_cancel()

        elif choice == "7":
            BR.Rescheduling_Booking()

        elif choice == "8":
            RA.record_attendance()

        elif choice == "9":
            VMAH.member_attendance_history()
        
        elif choice == "10":
            VBR.view_booking_request()
        
        elif choice == "11":
            return
            
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    booking_officer_menu()