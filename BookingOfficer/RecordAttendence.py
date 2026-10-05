#Record Attendance
from BookingOfficer import Function as F
def record_attendance():

    
    while True:
        print(f"""
          {"=" * 40}
          Record Attendance
          
          1. record attendance
          2. Back to Booking Officer Menu
          {"=" * 40}
          """)
        choice = input("Enter Choice")
        if choice == "1":
            bookingID = input("Enter booking ID: ").strip()
            if not F.check_bookingID(bookingID):
                print("Invalid Booking ID")
                return
            try:
                with open("txt/Booking.txt", "r") as file:

                    for line in file:
                        data = line.strip().split(",")
                        if len(data) == 7:

                            if data[0] == bookingID:
                                if data[6] != "Booked":
                                    print("This booking is not active.")
                                    return

                            print("Member ID:", data[1])
                            print("Class ID:", data[2])

                            while True:

                                print("\n1. Present")
                                print("2. Absent")

                                choice = input("Enter attendance: ").strip()

                                if choice == "1":
                                    attendance = "Present"
                                    break

                                elif choice== "2":
                                    attendance = "Absent"
                                    break

                                else:
                                    print("Invalid choice - TRY AGAIN")

                            with open("txt/Attendance.txt", "a") as file:

                                file.write(
                                    bookingID + ","
                                    + data[1] + ","
                                    + data[2] + ","
                                    + attendance + "\n"
                                    )

                            print("Attendance recorded successfully.")
                            break
            except FileNotFoundError:
                print("Booking file not found.")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")