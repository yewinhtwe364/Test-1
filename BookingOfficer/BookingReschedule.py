# Reschedule booking
from BookingOfficer import Function as F
def Rescheduling_Booking():

    
    while True:
        print(f"""
                {"=" * 40}
                Reschedule Booking
                
                1. Reschedule Booking
                2. Back to Booking Officer Menu
                {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            bookingID = input("Enter booking ID: ").strip()
            if not F.check_bookingID(bookingID):
                print("Invalid Booking ID")
                return
            booking = F.get_booking(bookingID)
            if booking is None:
                print("Wrong Data in this booking")
            else:
                print(f"""
                      Current Booking Status
                      BookingID = {booking[0]}
                      MemberID = {booking[1]}
                      ClassID = {booking[2]}
                      Booking Date = {booking[3]}
                      Booking Time = {booking[4]}
                      Lecturer = {booking[5]}
                      Status = {booking[6]}
                      """)
                if booking[6] != "Booked":
                    print("This Booking is inactive, Can't be rescheduled")
                    return
            new_class_id = booking[2]
            Date = booking[3]
            updated = False
            print("""
                    Reschedule Option
                    1. Class Reschedule
                    2. Date Reschedule
                    3. Exit
                    """)
            while True:
               
                choice = input("Enter Choice: ")
                if choice == "1":
                    
                    new_class_id = input("Enter new class ID: ").strip()

                    new_class = F.get_class(new_class_id)

                    if new_class is None:
                        print("New class does not exist.")
                    else:
                        updated = True
                        print("New class selected")
                elif choice == "2":
                    while True:
                        Date = input("Enter New Date: ").strip()                       
                        if not F.check_date(Date):
                            print("Invalid Date: ")
                        else:
                            updated = True
                            print("New Date is selected")
                            break
                elif choice == "3":
                    break
                else:
                    print("Wrong Choice , Please Enter Againg: ")
            if updated:
                try:
                    with open("txt/Booking.txt", "r") as file:
                        lines = file.readlines()

                    found = False

                    with open("txt/Booking.txt", "w") as file:

                        for line in lines:

                            data = line.strip().split(",")

                            if len(data) == 7:

                                if data[0] == bookingID and data[6] == "Booked":

                                    data[2] = new_class_id
                                    data[3] = Date
                                    data[4] = new_class[2]
                                    data[5] = new_class[3]

                                    found = True

                            file.write(",".join(data) + "\n")

                    if found:
                        print("Booking rescheduled successfully.")
                    else:
                        print("Booking not found.")

                except FileNotFoundError:
                    print("Booking file not found.")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")
