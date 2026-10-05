from BookingOfficer import Function as F
def delete_booking():
    
    while True:
        print(f"""
          {"=" * 40}
          Delete Booking
          
          1. delete booking
          2. back to Booking Officer Menu
          {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            try:
                booking_id = input("Enter BookingID : ")
                if not F.check_bookingID(booking_id):
                    print("Invalid BookingID")
                    return
                records = []
                with open("txt/Booking.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        if data[0] != booking_id:
                            records.append(data)
                    with open("txt/Booking.txt", "w") as file:
                        for record in records:
                            file.write(",".join(record)+ "\n")
                    print(f"BookingID {booking_id} has successfully deleted")
            except FileNotFoundError:
                print("file not found")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")