from Member import Function as F
def view_booking_history(memberID):
    while True:
        print(f"""
              {"=" * 40}
              View Booking History
              
              1. view booking history
              2. back
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            try:
                with open("txt/Booking.txt", "r") as file:
                    lines = file.readlines()
                    if len(lines) == 0:
                        print("No Data in the file")
                        continue
                    else:
                        print(f"{"BookingID":<10}{"ClassID":<10}{"ClassName":<30}{"Lecturer":<30}{"Booking Date":<15}{"Booking Time":<30}{"Booking Status":<15}")
                        for line in lines:
                            data = line.strip().split(",")
                            if len(data) < 7:
                                print(f"Incomplete Data: {data}")
                                continue

                            if data[1] == memberID:
                                classdata = F.get_class(data[2])
                                if classdata is None:
                                    className = "N/A"
                                else:
                                    className = classdata[1]
                                print(f"{data[0]:<10}{data[2]:<10}{className:<30}{data[5]:<30}{data[3]:<15}{data[4]:<30}{data[6]:<15}")
            except FileNotFoundError:
                print("Flie is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")