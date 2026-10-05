# View Attendance History
from BookingOfficer import Function as F
def member_attendance_history():
    
    while True:
        print(f"""
          {"=" * 40}
          View Attendance History
          
          1. view attendance history
          2. back to Booking Officer Menu
          {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            member_id = input("Enter member ID: ").strip()
            if not F.check_member(member_id):
                print("Invalid Member ID")
                return 
            else:
                try:
                    with open("txt/Attendance.txt", "r") as file:
                        print(f"{"Booking ID":<15}{"Member ID":<15}{"Class ID":<15}{"Attendance":<15}")
                        for line in file:
                            data = line.strip().split(",")
                            if len(data) == 4 and data[1] == member_id:
                                print(f"{data[0]:<15}{data[1]:<15}{data[2]:<15}{data[3]:<15}")
                except FileNotFoundError:
                    print("file is not found.")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")