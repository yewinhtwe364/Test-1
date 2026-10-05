from BookingOfficer import Function as F
def booking_cancel():
    while True:
        print(f"""
              {"=" * 40}
              Booking Cancelling
              
              1. Booking Cancel
              2. back
              {"=" * 40}
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            bookingID = input("Enter Booking: ").strip()
            if not F.check_bookingID(bookingID):
                print("Invalid Booking ID")
                return
            else:
                found = False
                record = []
                try:
                    with open("txt/Booking.txt", "r") as file:
                        for line in file:
                            data = line.strip().split(",")
                            if len(data) >= 7:
                                if data[0] == bookingID and data[6].strip().lower() == "booked":
                                    data[6] = "Cancelled"
                                    found = True
                            record.append(",".join(data))
                        if found:
                            
                            with open("txt/Booking.txt", "w") as file:
                                for line in record:
                                    file.write(line +"\n")
                                print("Booking is cancelled successfully!")
                        else:
                            print("booking is already cancelled")
                except FileNotFoundError:
                    print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice!")
