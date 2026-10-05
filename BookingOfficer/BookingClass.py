# Booking class
from BookingOfficer import Function as F
def class_booking():

    
    while True:
        print(f"""
          {"=" * 40}
           Booking Class
          
          1. booking class
          2. back to Booking Officer Menu
          {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            member_id = input("\nEnter member ID: ").strip()
            if not F.check_member(member_id):
                print("Member does not exist.")
                return
            class_id = input("Enter class ID: ").strip()
            class_data = F.get_class(class_id)
            if class_data is None:
                print("Class does not exist.")
                return

            while True:
                
                Date = input("Enter Booking Date: ").strip()
                if not F.check_date(Date):
                    print("Invalid Date: ")
                else:
                    break
            
            if F.already_booked(member_id, class_id):
                print("Member already booked this class.")
                return

            capacity = int(class_data[4])
            current_bookings = F.count_class_bookings(class_id)
            booking_id = F.generate_booking_id()

            if current_bookings >= capacity:

                print("Class is full.")
                print("Member will be placed on the waitlist.")
                try:

                    with open("txt/Booking.txt", "a") as file:

                        file.write(
                            booking_id + ","
                            + member_id + ","
                            + class_id + ","
                            + Date + ","
                            + class_data[2] + ","
                            + class_data[3] + ",Waitlist\n"
                        )

                    print("Added to waitlist.")
                    print("Booking ID:", booking_id)
                except FileNotFoundError:
                    print("file is not found!")

            else:
                try:

                    with open("txt/Booking.txt", "a") as file:

                        file.write(
                            booking_id + ","
                            + member_id + ","
                            + class_id + ","
                            + Date + ","
                            + class_data[2] + ","
                            + class_data[3] + ",Booked\n"
                        )

                    print("Booking successful.")
                    print("Booking ID:", booking_id)
                except FileNotFoundError:
                    print("file is not found")
        elif choice == "2":
            return
        else:
            print("Wrong Choice ")
            

